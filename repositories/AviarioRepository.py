from sqlalchemy import select

from helpers.database import db
from helpers.logger import logger
from models.Aviario import Aviario


class AviarioRepository:
    def get_all(self, filtros: dict = None):
        stmt = select(Aviario)
        if filtros:
            stmt = stmt.filter_by(**filtros)
        return db.session.execute(stmt).scalars().all()

    def get_by_id(self, id):
        logger.info(f"Consultando aviario pelo id.")
        return db.session.get(Aviario, id)

    def insert(self, nome, capacidae, tipo, avicola_id):
        aviario = Aviario(nome, capacidae, tipo, avicola_id)
        db.session.add(aviario)
        db.session.commit()
        logger.info(f"Aviario inserido com o id: {aviario.id}")
        return aviario

    def update(self, id, nome, capacidae, tipo, avicola_id):
        aviario = db.session.get(Aviario, id)
        if aviario is None:
            return None
        aviario.nome = nome
        aviario.capacidae = capacidae
        aviario.tipo = tipo
        aviario.avicola_id = avicola_id
        db.session.commit()
        logger.info(f"Aviario atualizado com o id: {id}")
        return aviario

    def delete(self, id):
        aviario = db.session.get(Aviario, id)
        if aviario is None:
            return False
        db.session.delete(aviario)
        db.session.commit()
        return True