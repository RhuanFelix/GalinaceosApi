from models.NomeTerritorio import NomeTerritorio
from repositories.NomeTerritorioRepository import NomeTerritorioRepository

def rowToNomeTerritorio(row):
    id, nome = row
    return NomeTerritorio(id, nome)

class NomeTerritorioService:
    def __init__(self):
        self.repository = NomeTerritorioRepository()

    def getById(self, id):
        row = self.repository.getById(id)
        return rowToNomeTerritorio(row) if row else None

    def getAll(self):
        rows = self.repository.getAll()
        return [rowToNomeTerritorio(r) for r in rows]

    def create(self, data):
        nome = data["nome"]
        id = self.repository.create(nome)
        return NomeTerritorio(id, nome)

    def update(self, id, data):
        affected = self.repository.update(id, data["nome"])
        if affected == 0:
            return None
        return NomeTerritorio(id, data["nome"])

    def delete(self, id):
        return self.repository.delete(id) > 0