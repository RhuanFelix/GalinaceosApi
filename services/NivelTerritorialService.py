from models.NivelTerritorial import NivelTerritorial
from repositories.NivelTerritorialRepository import NivelTerritorialRepository

def rowToNivelTerritorial(row):
    id, sigla, descricao = row
    return NivelTerritorial(id, sigla, descricao)

class NivelTerritorialService:
    def __init__(self):
        self.repository = NivelTerritorialRepository()

    def getById(self, id):
        row = self.repository.getById(id)
        return rowToNivelTerritorial(row) if row else None

    def getAll(self):
        rows = self.repository.getAll()
        return [rowToNivelTerritorial(r) for r in rows]

    def create(self, data):
        sigla = data["sigla"]
        descricao = data["descricao"]
        id = self.repository.create(sigla, descricao)
        return NivelTerritorial(id, sigla, descricao)

    def update(self, id, data):
        affected = self.repository.update(id, data["sigla"], data["descricao"])
        if affected == 0:
            return None
        return NivelTerritorial(id, data["sigla"], data["descricao"])

    def delete(self, id):
        return self.repository.delete(id) > 0