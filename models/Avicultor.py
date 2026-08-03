from datetime import datetime

from flask_restful import fields as dto
from marshmallow import Schema, fields, validate
from sqlalchemy import String, DateTime, Integer, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship

from helpers.database import db


avicultor_fields = {
    'id': dto.Integer,
    'nome': dto.String,
    'nascimento': dto.DateTime(dt_format='iso8601'),
    'cpf': dto.String,
    'caf': dto.String,
}

avicultor_id_fields = {
    'id': dto.Integer,
}

class Avicultor(db.Model):
    __tablename__ = 'tb_avicultor'

    id: Mapped[int] = mapped_column('id', primary_key=True)
    nome: Mapped[str] = mapped_column('nome', String())
    nascimento: Mapped[datetime] = mapped_column('nascimento', DateTime)
    cpf: Mapped[str] = mapped_column('cpf', String(11))
    caf: Mapped[str] = mapped_column('caf', String())
    avicola_id: Mapped[int] = mapped_column(ForeignKey('tb_avicola.id'))
    avicola: Mapped['Avicola'] = relationship(back_populates='avicultores')

    def __init__(self, nome, nascimento, cpf, caf, avicola_id):
        self.nome = nome
        self.nascimento = nascimento
        self.cpf = cpf
        self.caf = caf
        self.avicola_id = avicola_id

    def toDict(self):
        return {
            'id': self.id,
            'nome': self.nome,
            'nascimento': self.nascimento,
            'cpf': self.cpf,
            'caf': self.caf,
            'avicola_id': self.avicola_id
        }

class AvicultorSchema(Schema):
    nome = fields.Str(required=True, error_messages={'required':'Adicione um nome'})
    nascimento = fields.Date(required=True)
    cpf = fields.Str(required=True, validate=validate.Length(max=11, error='Tamanho do CPF inválido.'), error_messages={'required': 'Adicione um CPF.', 'invalid':'Valor inválido.'})
    caf = fields.Str(required=True)
    avicola_id = fields.Int(required=True)