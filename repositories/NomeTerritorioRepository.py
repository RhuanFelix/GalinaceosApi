from helpers.database import get_conn

class NomeTerritorioRepository:
    def getById(self, id):
        conn = get_conn()
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM nome_territorio WHERE id=%s", (id,))
        return cursor.fetchone()

    def getAll(self):
        conn = get_conn()
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM nome_territorio")
        return cursor.fetchall()

    def create(self, nome):
        conn = get_conn()
        cursor = conn.cursor()
        cursor.execute("INSERT INTO nome_territorio(nome) VALUES(%s)", (nome,))
        conn.commit()
        return cursor.lastrowid

    def update(self, id, nome):
        conn = get_conn()
        cursor = conn.cursor()
        cursor.execute("UPDATE nome_territorio SET nome=%s WHERE id=%s", (nome, id))
        conn.commit()
        return cursor.rowcount

    def delete(self, id):
        conn = get_conn()
        cursor = conn.cursor()
        cursor.execute("DELETE FROM nome_territorio WHERE id=%s", (id,))
        conn.commit()
        return cursor.rowcount