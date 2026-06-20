from helpers.database import get_conn

class NivelTerritorialRepository:
    def getById(self, id):
        conn = get_conn()
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM nivel_territorial WHERE id=%s", (id,))
        return cursor.fetchone()

    def getAll(self):
        conn = get_conn()
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM nivel_territorial")
        return cursor.fetchall()

    def create(self, sigla, descricao):
        conn = get_conn()
        cursor = conn.cursor()
        cursor.execute("INSERT INTO nivel_territorial(sigla, descricao) VALUES(%s, %s)", (sigla, descricao))
        conn.commit()
        return cursor.lastrowid

    def update(self, id, sigla, descricao):
        conn = get_conn()
        cursor = conn.cursor()
        cursor.execute("UPDATE nivel_territorial SET sigla=%s, descricao=%s WHERE id=%s", (sigla, descricao, id))
        conn.commit()
        return cursor.rowcount

    def delete(self, id):
        conn = get_conn()
        cursor = conn.cursor()
        cursor.execute("DELETE FROM nivel_territorial WHERE id=%s", (id,))
        conn.commit()
        return cursor.rowcount