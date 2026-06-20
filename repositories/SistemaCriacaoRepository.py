from helpers.database import get_conn


class SistemaCriacaoRepository:
    def getById(self, id):
        conn = get_conn()
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM sistema_criacao WHERE id=%s", (id,))
        return cursor.fetchone()

    def getAll(self):
        conn = get_conn()
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM sistema_criacao")
        return cursor.fetchall()

    def create(self, sigla, descricao):
        conn = get_conn()
        cursor = conn.cursor()
        cursor.execute("INSERT INTO sistema_criacao(sigla, descricao) VALUES(%s, %s)", (sigla, descricao))
        conn.commit()
        return cursor.lastrowid

    def update(self, id, sigla, descricao):
        conn = get_conn()
        cursor = conn.cursor()
        cursor.execute("UPDATE sistema_criacao SET sigla=%s, descricao=%s WHERE id=%s", (sigla, descricao, id))
        conn.commit()
        return cursor.rowcount

    def delete(self, id):
        conn = get_conn()
        cursor = conn.cursor()
        cursor.execute("DELETE FROM sistema_criacao WHERE id=%s", (id,))
        conn.commit()
        return cursor.rowcount