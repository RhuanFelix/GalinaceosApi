from sqlalchemy import select

from helpers.database import db
from helpers.logger import logger
from models.Galpao import Galpao


class GalpaoRepository:
    def get_all(self, filtros: dict = None):
        stmt = select(Galpao)
        if filtros:
            stmt = stmt.filter_by(**filtros)
        return db.session.execute(stmt).scalars().all()

    def get_by_id(self, id):
        logger.info(f"Consultando galpão pelo id.")
        return db.session.get(Galpao, id)

    def insert(self, codigo, area_m2, aviario_id):
        galpao = Galpao(codigo, area_m2, aviario_id)
        db.session.add(galpao)
        db.session.commit()
        logger.info(f"Galpão inserido com o id: {galpao.id}")
        return galpao

    def update(self, id, codigo, area_m2, aviario_id):
        galpao = db.session.get(Galpao, id)
        if galpao is None:
            return None
        galpao.codigo = codigo
        galpao.area_m2 = area_m2
        galpao.aviario_id = aviario_id
        db.session.commit()
        logger.info(f"Galpão atualizado com o id: {id}")
        return galpao

    def delete(self, id):
        galpao = db.session.get(Galpao, id)
        if galpao is None:
            return False
        db.session.delete(galpao)
        db.session.commit()
        return True