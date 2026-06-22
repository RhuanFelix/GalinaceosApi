import pandas as pd
import numpy as np
import psycopg2
from psycopg2 import sql
from psycopg2.extras import execute_values
import os
from dotenv import load_dotenv

load_dotenv()

def get_connection():
    """Estabelece conexão com o banco de dados PostgreSQL"""
    return psycopg2.connect(
        database=os.getenv("DB_NAME"),
        user=os.getenv("DB_USER"),
        password=os.getenv("DB_PASSWORD"),
        host=os.getenv("DB_HOST"),
        port=os.getenv("DB_PORT")
    )

df = pd.read_csv(
    'GALINACEOS.csv',
    sep=';',
    encoding='latin1',
    dtype=str,
    keep_default_na=False
)

df.columns = df.columns.str.lower()

df = df.replace(r'^\s*$', np.nan, regex=True)
df = df.replace('X', np.nan)

df['sist_cria_sigla'] = df['sist_cria'].str.split('-').str[1]
dim_sist = (
    df[['sist_cria_sigla']]
    .drop_duplicates()
    .dropna()
    .rename(columns={'sist_cria_sigla': 'sigla'})
)
dim_sist['descricao'] = dim_sist['sigla']

dim_niv = (
    df[['niv_terr']]
    .drop_duplicates()
    .dropna()
    .rename(columns={'niv_terr': 'sigla'})
)
dim_niv['descricao'] = dim_niv['sigla']

dim_cod = (
    df[['cod_terr', 'nom_terr']]
    .drop_duplicates()
    .dropna(subset=['cod_terr'])
)
dim_cod['cod_terr'] = dim_cod['cod_terr'].astype(float).astype('Int64')
dim_cod = dim_cod.rename(columns={'cod_terr': 'codigo', 'nom_terr': 'descricao'})

dim_nom = (
    df[['nom_terr']]
    .drop_duplicates()
    .dropna()
    .rename(columns={'nom_terr': 'nome'})
)

dim_cl = (
    df[['cl_gal', 'nom_cl_gal']]
    .drop_duplicates()
    .dropna(subset=['cl_gal'])
)
dim_cl['cl_gal'] = dim_cl['cl_gal'].astype(int)
dim_cl = dim_cl.rename(columns={'cl_gal': 'codigo', 'nom_cl_gal': 'descricao'})

conn = get_connection()
conn.autocommit = False
cur = conn.cursor()

try:
    cur.execute("TRUNCATE TABLE tb_avicultura_2017 CASCADE;")
    cur.execute("TRUNCATE TABLE sistema_criacao, nivel_territorial, "
                "codigo_territorial, nome_territorio, classe_cabeca_galinaceos CASCADE;")
    conn.commit()

    def insert_dim(table_name, columns, data):
        if data.empty:
            return
        records = [tuple(None if pd.isna(v) else v for v in row)
                   for row in data.to_numpy()]
        cols = sql.SQL(', ').join(map(sql.Identifier, columns))
        sql_stmt = sql.SQL("INSERT INTO {} ({}) VALUES %s").format(
            sql.Identifier(table_name), cols
        )
        execute_values(cur, sql_stmt, records)

    insert_dim('sistema_criacao', ['sigla', 'descricao'], dim_sist)
    insert_dim('nivel_territorial', ['sigla', 'descricao'], dim_niv)
    insert_dim('codigo_territorial', ['codigo', 'descricao'], dim_cod)
    insert_dim('nome_territorio', ['nome'], dim_nom)
    insert_dim('classe_cabeca_galinaceos', ['codigo', 'descricao'], dim_cl)
    conn.commit()

    def get_map(column, table):
        cur.execute(f"SELECT id, {column} FROM {table}")
        return {row[1]: row[0] for row in cur.fetchall()}

    map_sist = get_map('sigla', 'sistema_criacao')
    map_niv  = get_map('sigla', 'nivel_territorial')
    map_cod  = get_map('codigo', 'codigo_territorial')
    map_nom  = get_map('nome', 'nome_territorio')
    map_cl   = get_map('codigo', 'classe_cabeca_galinaceos')

    df['sist_cria'] = df['sist_cria_sigla'].map(map_sist)
    df['niv_terr']  = df['niv_terr'].map(map_niv)
    df['cod_terr']  = pd.to_numeric(df['cod_terr'], errors='coerce').map(map_cod)
    df['nom_terr']  = df['nom_terr'].map(map_nom)
    df['cl_gal']    = pd.to_numeric(df['cl_gal'], errors='coerce').map(map_cl)

    colunas_fato = [
        'sist_cria', 'niv_terr', 'cod_terr', 'nom_terr', 'cl_gal',
        'e_cria_gal', 'e_tem_gal', 'e_gal_vend', 'e_ovos_prod', 'e_ovos_vend',
        'e_subs', 'e_comerc', 'e_recebe_ori', 'e_ori_gov', 'e_ori_propria',
        'e_ori_coop', 'e_ori_emp_int', 'e_ori_emp_priv', 'e_ori_ong', 'e_ori_sist_s',
        'e_ori_outra', 'e_gal_eng', 'e_gal_galos', 'e_gal_poed', 'e_gal_matr',
        'e_assoc_coop', 'e_financ', 'e_financ_coop', 'e_financ_integ', 'e_dap',
        'e_agrifam', 'e_n_agrifam', 'e_produtor', 'e_cooperativa', 'e_sa_ldta',
        'e_cnpj', 'gal_total', 'gal_eng', 'gal_galos', 'gal_poed', 'gal_matr',
        'gal_vend', 'v_gal_vend', 'q_dz_prod', 'q_dz_vend', 'v_q_dz_prod',
        'v_q_dz_vend', 'a_total', 'a_past_plant', 'a_lav_perm', 'a_lav_temp',
        'a_apprl', 'vtp_agro', 'rect_agro', 'n_trab_total', 'n_trab_lacos'
    ]

    df_fato = df[colunas_fato].copy()
    dados_fato = [
        [None if pd.isna(v) else v for v in row]
        for row in df_fato.to_numpy()
    ]

    col_names = sql.SQL(', ').join(map(sql.Identifier, colunas_fato))
    insert_sql = sql.SQL("INSERT INTO tb_avicultura_2017 ({}) VALUES %s").format(col_names)

    chunk_size = 5000
    for i in range(0, len(dados_fato), chunk_size):
        chunk = dados_fato[i:i + chunk_size]
        execute_values(cur, insert_sql, chunk)
        conn.commit()
        print(f"Lote {i//chunk_size + 1} inserido ({len(chunk)} registros)")

    print("Carga concluída com sucesso!")

except Exception as e:
    conn.rollback()
    print(f"Erro durante a carga: {e}")
    raise
finally:
    cur.close()
    conn.close()