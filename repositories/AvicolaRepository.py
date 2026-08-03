from sqlalchemy import select

from helpers.database import db
from helpers.logger import logger
from models.Avicola import Avicola


class AvicolaRepository:
    def get_all(self, filtros: dict = None):
        stmt = select(Avicola)
        if filtros:
            stmt = stmt.filter_by(**filtros)
        return db.session.execute(stmt).scalars().all()

    def get_by_id(self, id):
        logger.info(f"Consultando avicola pelo id.")
        return db.session.get(Avicola, id)

    def insert(self, nome, endereco, telefone):
        avicola = Avicola(nome, endereco, telefone)
        db.session.add(avicola)
        db.session.commit()
        logger.info(f"Avicola inserida com o id: {avicola.id}")
        return avicola

    def update(self, id, nome, endereco, telefone):
        avicola = db.session.get(Avicola, id)
        if avicola is None:
            return None
        avicola.nome = nome
        avicola.endereco = endereco
        avicola.telefone = telefone
        db.session.commit()
        logger.info(f"Avicola atualizada com o id: {id}")
        return avicola

    def delete(self, id):
        avicola = db.session.get(Avicola, id)
        if avicola is None:
            return False
        db.session.delete(avicola)
        db.session.commit()
        return True