from sqlalchemy import select

from helpers.database import db
from helpers.logger import logger
from models.Avicultor import Avicultor


class AvicultorRepository:
    def get_all(self, filtros: dict = None):
        stmt = select(Avicultor)
        if filtros:
            stmt = stmt.filter_by(**filtros)
        return db.session.execute(stmt).scalars().all()

    def get_by_id(self, id):
        logger.info(f"Consultando avicultor pelo id.")
        return db.session.get(Avicultor, id)

    def insert(self, nome, nascimento, cpf, caf, avicola_id):
        avicultor = Avicultor(nome, nascimento, cpf, caf, avicola_id)
        db.session.add(avicultor)
        db.session.commit()
        logger.info(f"Avicultor inserido com o id: {avicultor.id}")
        return avicultor

    def update(self, id, nome, nascimento, cpf, caf, avicola_id):
        avicultor = db.session.get(Avicultor, id)
        if avicultor is None:
            return None
        avicultor.nome = nome
        avicultor.nascimento = nascimento
        avicultor.cpf = cpf
        avicultor.caf = caf
        avicultor.avicola_id = avicola_id
        db.session.commit()
        logger.info(f"Avicultor atualizado com o id: {id}")
        return avicultor

    def delete(self, id):
        avicultor = db.session.get(Avicultor, id)
        if avicultor is None:
            return False
        db.session.delete(avicultor)
        db.session.commit()
        return True