from flask_restful import fields as dto
from marshmallow import Schema, fields
from sqlalchemy import Integer, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship

from helpers.database import db


galpao_fields = {
    'id': dto.Integer,
    'codigo': dto.Integer,
    'area_m2': dto.Integer,
}

galpao_id_fields = {
    'id': dto.Integer
}

class Galpao(db.Model):
    __tablename__ = 'tb_galpao'

    id: Mapped[int] = mapped_column('id', primary_key=True)
    codigo: Mapped[int] = mapped_column('codigo', Integer())
    area_m2: Mapped[int] = mapped_column('area_m2', Integer())
    aviario_id: Mapped[int] = mapped_column(ForeignKey('tb_aviario.id'))
    aviario: Mapped['Aviario'] = relationship(back_populates='galpoes')

    def __init__(self, codigo, area_m2, aviario_id):
        self.codigo = codigo
        self.area_m2 = area_m2
        self.aviario_id = aviario_id

    def toDict(self):
        return {
            'id': self.id,
            'codigo': self.codigo,
            'area_m2': self.area_m2,
            'aviario_id': self.aviario_id
        }

class GalpaoSchema(Schema):
    codigo = fields.Int(required=True)
    area_m2 = fields.Int(required=True)
    aviario_id = fields.Int(required=True)