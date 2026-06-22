from helpers.database import get_conn

class Avicultura2017Repository:
    def get_by_filters(self, filters):
        """
        Busca registros de avicultura 2017 com filtros opcionais.
        Filtros aceitos: sist_cria, niv_terr, cod_terr, nom_terr, cl_gal
        """
        conn = get_conn()
        cur = conn.cursor()
        
        # Construir query base
        query = "SELECT * FROM tb_avicultura_2017 WHERE 1=1"
        params = []
        
        # Adicionar filtros dinamicamente
        if filters.get('sist_cria'):
            query += " AND sist_cria = %s"
            params.append(int(filters['sist_cria']))
        
        if filters.get('niv_terr'):
            query += " AND niv_terr = %s"
            params.append(int(filters['niv_terr']))
        
        if filters.get('cod_terr'):
            query += " AND cod_terr = %s"
            params.append(int(filters['cod_terr']))
        
        if filters.get('nom_terr'):
            query += " AND nom_terr = %s"
            params.append(int(filters['nom_terr']))
        
        if filters.get('cl_gal'):
            query += " AND cl_gal = %s"
            params.append(int(filters['cl_gal']))
        
        query += " LIMIT 100"
        
        try:
            cur.execute(query, params)
            rows = cur.fetchall()
            return rows
        finally:
            cur.close()