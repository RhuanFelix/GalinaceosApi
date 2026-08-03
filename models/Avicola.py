from typing import List

from flask_restful import fields as dto
from marshmallow import Schema, fields, validate
from sqlalchemy import String, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship

from helpers.database import db


avicola_fields = {
    'id': dto.Integer,
    'nome': dto.String,
    'endereco': dto.String,
    'telefone': dto.String,
}

avicola_id_fields = {
    'id': dto.Integer,
}

class Avicola(db.Model):
    __tablename__ = 'tb_avicola'

    id: Mapped[int] = mapped_column('id', primary_key=True)
    nome: Mapped[str] = mapped_column('nome', String())
    endereco: Mapped[str] = mapped_column('endereco', String())
    telefone: Mapped[str] = mapped_column('telefone', String(11))
    avicultores: Mapped[List['Avicultor']] = relationship(back_populates='avicola', cascade='all, delete-orphan')
    aviarios: Mapped[List['Aviario']] = relationship(back_populates='avicola', cascade='all, delete-orphan')

    def __init__(self, nome, endereco, telefone):
        self.nome = nome
        self.endereco = endereco
        self.telefone = telefone

    def toDict(self):
        return {
            'id': self.id,
            'nome': self.nome,
            'endereco': self.endereco,
            'telefone': self.telefone,
        }

class AvicolaSchema(Schema):
    nome = fields.Str(required=True, error_messages={'required':'Adicione um nome'})
    endereco = fields.Str(required=True)
    telefone = fields.Str(required=True, validate=validate.Length(max=11))
