from models.CodigoTerritorial import CodigoTerritorial
from repositories.CodigoTerritorialRepository import CodigoTerritorialRepository

def rowToCodigoTerritorial(row):
    id, codigo, descricao = row
    return CodigoTerritorial(id, codigo, descricao)

class CodigoTerritorialService:
    def __init__(self):
        self.repository = CodigoTerritorialRepository()

    def getById(self, id):
        row = self.repository.getById(id)
        return rowToCodigoTerritorial(row) if row else None

    def getAll(self):
        rows = self.repository.getAll()
        return [rowToCodigoTerritorial(r) for r in rows]

    def create(self, data):
        codigo = data["codigo"]
        descricao = data["descricao"]
        id = self.repository.create(codigo, descricao)
        return CodigoTerritorial(id, codigo, descricao)

    def update(self, id, data):
        affected = self.repository.update(id, data["codigo"], data["descricao"])
        if affected == 0:
            return None
        return CodigoTerritorial(id, data["codigo"], data["descricao"])

    def delete(self, id):
        return self.repository.delete(id) > 0