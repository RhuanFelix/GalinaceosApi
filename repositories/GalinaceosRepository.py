from sqlalchemy import select

from helpers.database import db
from models.Galinaceos import Galinaceos


class GalinaceosRepository:
    def get_all(self, filtros: dict = None):
        stmt = select(Galinaceos)
        if filtros:
            stmt = stmt.filter_by(**filtros)
        return db.session.execute(stmt).scalars().all()