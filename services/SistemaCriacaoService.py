from models.SistemaCriacao import SistemaCriacao
from repositories.SistemaCriacaoRepository import SistemaCriacaoRepository


def rowToSistemaCriacao(row):
    id = row[0]
    sigla = row[1]
    descricao = row[2]
    return SistemaCriacao(id, sigla, descricao)

class SistemaCriacaoService:
    def __init__(self):
        self.sistemaCriacaoRepository = SistemaCriacaoRepository()

    def getById(self, id):
        row = self.sistemaCriacaoRepository.getById(id)
        return rowToSistemaCriacao(row) if row is not None else None

    def getAll(self):
        rows = self.sistemaCriacaoRepository.getAll()
        return [rowToSistemaCriacao(r) for r in rows]

    def create(self, data):
        sigla = data["sigla"]
        descricao = data["descricao"]
        id = self.sistemaCriacaoRepository.create(sigla, descricao)
        return SistemaCriacao(id, sigla, descricao)

    def update(self, id, data):
        affected = self.sistemaCriacaoRepository.update(id, data["sigla"], data["descricao"])
        if affected == 0:
            return None
        return SistemaCriacao(id, data["sigla"], data["descricao"])

    def delete(self, id):
        affected = self.sistemaCriacaoRepository.delete(id)
        return affected > 0