from helpers.database import get_conn

class CodigoTerritorialRepository:
    def getById(self, id):
        conn = get_conn()
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM codigo_territorial WHERE id=%s", (id,))
        return cursor.fetchone()

    def getAll(self):
        conn = get_conn()
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM codigo_territorial")
        return cursor.fetchall()

    def create(self, codigo, descricao):
        conn = get_conn()
        cursor = conn.cursor()
        cursor.execute("INSERT INTO codigo_territorial(codigo, descricao) VALUES(%s, %s)",(codigo, descricao))
        conn.commit()
        return cursor.lastrowid

    def update(self, id, codigo, descricao):
        conn = get_conn()
        cursor = conn.cursor()
        cursor.execute("UPDATE codigo_territorial SET codigo=%s, descricao=%s WHERE id=%s",(codigo, descricao, id))
        conn.commit()
        return cursor.rowcount

    def delete(self, id):
        conn = get_conn()
        cursor = conn.cursor()
        cursor.execute("DELETE FROM codigo_territorial WHERE id=%s", (id,))
        conn.commit()
        return cursor.rowcount