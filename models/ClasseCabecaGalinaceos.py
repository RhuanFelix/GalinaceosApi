from marshmallow import Schema, fields

class ClasseCabecaGalinaceos:
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

class ClasseCabecaGalinaceosSchema(Schema):
    codigo = fields.Int(required=True)
    descricao = fields.Str(required=True)