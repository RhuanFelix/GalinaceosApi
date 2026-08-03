from typing import List

from flask_restful import fields as dto
from marshmallow import Schema, fields
from sqlalchemy import String, Integer, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship

from helpers.database import db


aviario_fields = {
    'id': dto.Integer,
    'nome': dto.String,
    'capacidade': dto.Integer,
    'tipo': dto.String,
}

aviario_id_fields = {
    'id': dto.Integer,
}

class Aviario(db.Model):
    __tablename__ = 'tb_aviario'

    id: Mapped[int] = mapped_column('id', primary_key=True)
    nome: Mapped[str] = mapped_column('nome', String())
    capacidade: Mapped[int] = mapped_column('capacidade', Integer())
    tipo: Mapped[str] = mapped_column('tipo', String())
    avicola_id: Mapped[int] = mapped_column(ForeignKey('tb_avicola.id'))
    avicola: Mapped['Avicola'] = relationship(back_populates='aviarios')
    galpoes: Mapped[List['Galpao']] = relationship(back_populates='aviario')

    def __init__(self, nome, capacidade, tipo, avicola_id):
        self.nome = nome
        self.capacidade = capacidade
        self.tipo = tipo
        self.avicola_id = avicola_id

    def toDict(self):
        return {
            'id': self.id,
            'nome': self.nome,
            'capacidade': self.capacidade,
            'tipo': self.tipo,
            'avicola_id': self.avicola_id
        }

class AviarioSchema(Schema):
    nome = fields.Str(required=True, error_messages={'required':'Adicione um nome'})
    capacidade = fields.Int(required=True)
    tipo = fields.Str(required=True)
    avicola_id = fields.Int(required=True)