CREATE TABLE IF NOT EXISTS sistema_criacao(
    id SERIAL PRIMARY KEY,
    sigla VARCHAR NOT NULL UNIQUE,
    descricao VARCHAR NOT NULL
);

CREATE TABLE IF NOT EXISTS nivel_territorial(
    id SERIAL PRIMARY KEY,
    sigla VARCHAR NOT NULL UNIQUE,
    descricao VARCHAR NOT NULL
);

CREATE TABLE IF NOT EXISTS codigo_territorial(
    id SERIAL PRIMARY KEY,
    codigo INT NOT NULL UNIQUE,
    descricao VARCHAR
);

CREATE TABLE IF NOT EXISTS nome_territorio(
    id SERIAL PRIMARY KEY,
    nome VARCHAR NOT NULL UNIQUE
);

CREATE TABLE IF NOT EXISTS classe_cabeca_galinaceos(
    id SERIAL PRIMARY KEY,
    codigo INT NOT NULL UNIQUE,
    descricao VARCHAR NOT NULL
);

-- Tabela para armazenar os dados do CSV de avicultura 2017
CREATE TABLE IF NOT EXISTS tb_avicultura_2017 (
    id SERIAL PRIMARY KEY,
    sist_cria INT,
    niv_terr  INT,
    cod_terr  INT,
    nom_terr  INT,
    cl_gal    INT,
    e_cria_gal       VARCHAR,
    e_tem_gal        VARCHAR,
    e_gal_vend       VARCHAR,
    e_ovos_prod      VARCHAR,
    e_ovos_vend      VARCHAR,
    e_subs           VARCHAR,
    e_comerc         VARCHAR,
    e_recebe_ori     VARCHAR,
    e_ori_gov        VARCHAR,
    e_ori_propria    VARCHAR,
    e_ori_coop       VARCHAR,
    e_ori_emp_int    VARCHAR,
    e_ori_emp_priv   VARCHAR,
    e_ori_ong        VARCHAR,
    e_ori_sist_s     VARCHAR,
    e_ori_outra      VARCHAR,
    e_gal_eng        VARCHAR,
    e_gal_galos      VARCHAR,
    e_gal_poed       VARCHAR,
    e_gal_matr       VARCHAR,
    e_assoc_coop     VARCHAR,
    e_financ         VARCHAR,
    e_financ_coop    VARCHAR,
    e_financ_integ   VARCHAR,
    e_dap            VARCHAR,
    e_agrifam        VARCHAR,
    e_n_agrifam      VARCHAR,
    e_produtor       VARCHAR,
    e_cooperativa    VARCHAR,
    e_sa_ldta        VARCHAR,
    e_cnpj           VARCHAR,
    gal_total        VARCHAR,
    gal_eng          VARCHAR,
    gal_galos        VARCHAR,
    gal_poed         VARCHAR,
    gal_matr         VARCHAR,
    gal_vend         VARCHAR,
    v_gal_vend       VARCHAR,
    q_dz_prod        VARCHAR,
    q_dz_vend        VARCHAR,
    v_q_dz_prod      VARCHAR,
    v_q_dz_vend      VARCHAR,
    a_total          VARCHAR,
    a_past_plant     VARCHAR,
    a_lav_perm       VARCHAR,
    a_lav_temp       VARCHAR,
    a_apprl          VARCHAR,
    vtp_agro         VARCHAR,
    rect_agro        VARCHAR,
    n_trab_total     VARCHAR,
    n_trab_lacos     VARCHAR,
    FOREIGN KEY (sist_cria) REFERENCES sistema_criacao(id),
    FOREIGN KEY (niv_terr) REFERENCES nivel_territorial(id),
    FOREIGN KEY (cod_terr) REFERENCES codigo_territorial(id),
    FOREIGN KEY (nom_terr) REFERENCES nome_territorio(id),
    FOREIGN KEY (cl_gal) REFERENCES classe_cabeca_galinaceos(id)
);