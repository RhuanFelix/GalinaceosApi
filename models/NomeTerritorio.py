from marshmallow import Schema, fields

class NomeTerritorio:
    def __init__(self, id, nome):
        self.id = id
        self.nome = nome

    def toDict(self):
        return {
            "id": self.id,
            "nome": self.nome,
        }

class NomeTerritorioSchema(Schema):
    nome = fields.Str(required=True)