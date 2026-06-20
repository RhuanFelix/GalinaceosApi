from marshmallow import Schema, fields

class CodigoTerritorial:
    def __init__(self, id, codigo, descricao):
        self.id = id
        self.codigo = codigo
        self.descricao = descricao

    def toDict(self):
        return {
            "id": self.id,
            "codigo": self.codigo,
            "descricao": self.descricao
        }

class CodigoTerritorialSchema(Schema):
    codigo = fields.Int(required=True)
    descricao = fields.Str(required=False)