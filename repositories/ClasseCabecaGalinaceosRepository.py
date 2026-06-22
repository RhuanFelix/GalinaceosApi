from helpers.database import get_conn

class ClasseCabecaGalinaceosRepository:
    def getById(self, id):
        conn = get_conn()
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM classe_cabeca_galinaceos WHERE id=%s", (id,))
        return cursor.fetchone()

    def getAll(self):
        conn = get_conn()
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM classe_cabeca_galinaceos")
        return cursor.fetchall()

    def create(self, codigo, descricao):
        conn = get_conn()
        cursor = conn.cursor()
        cursor.execute("INSERT INTO classe_cabeca_galinaceos(codigo, descricao) VALUES(%s, %s)", (codigo, descricao))
        conn.commit()
        return cursor.lastrowid

    def update(self, id, codigo, descricao):
        conn = get_conn()
        cursor = conn.cursor()
        cursor.execute("UPDATE classe_cabeca_galinaceos SET codigo=%s, descricao=%s WHERE id=%s", (codigo, descricao, id))
        conn.commit()
        return cursor.rowcount

    def delete(self, id):
        conn = get_conn()
        cursor = conn.cursor()
        cursor.execute("DELETE FROM classe_cabeca_galinaceos WHERE id=%s", (id,))
        conn.commit()
        return cursor.rowcount