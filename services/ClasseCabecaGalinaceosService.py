from models.ClasseCabecaGalinaceos import ClasseCabecaGalinaceos
from repositories.ClasseCabecaGalinaceosRepository import ClasseCabecaGalinaceosRepository

def rowToClasseCabecaGalinaceos(row):
    id, codigo, descricao = row
    return ClasseCabecaGalinaceos(id, codigo, descricao)

class ClasseCabecaGalinaceosService:
    def __init__(self):
        self.repository = ClasseCabecaGalinaceosRepository()

    def getById(self, id):
        row = self.repository.getById(id)
        return rowToClasseCabecaGalinaceos(row) if row else None

    def getAll(self):
        rows = self.repository.getAll()
        return [rowToClasseCabecaGalinaceos(r) for r in rows]

    def create(self, data):
        codigo = data["codigo"]
        descricao = data["descricao"]
        id = self.repository.create(codigo, descricao)
        return ClasseCabecaGalinaceos(id, codigo, descricao)

    def update(self, id, data):
        affected = self.repository.update(id, data["codigo"], data["descricao"])
        if affected == 0:
            return None
        return ClasseCabecaGalinaceos(id, data["codigo"], data["descricao"])

    def delete(self, id):
        return self.repository.delete(id) > 0