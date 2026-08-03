from helpers.logger import logger
from repositories.AvicolaRepository import AvicolaRepository


class AvicolaService:
    def __init__(self):
        self.avicola_repository = AvicolaRepository()

    def get_all(self, filtros: dict = None):
        avicolas = self.avicola_repository.get_all(filtros)
        logger.info(f"Retornando {len(avicolas)} avicolas.")
        return avicolas

    def get_by_id(self, id):
        avicola = self.avicola_repository.get_by_id(id)
        logger.info("Lendo informações do resultado da consulta ao banco")
        return avicola

    def create(self, data):
        avicola = self.avicola_repository.insert(data['nome'], data['endereco'], data['telefone'])
        logger.info(f"Avicola criada com id: {avicola.id}")
        return avicola

    def update(self, id, data):
        avicola = self.avicola_repository.update(id, data['nome'], data['endereco'], data['telefone'])
        if avicola is None:
            return None
        logger.info(f"Avicola atualizada com id: {id}")
        return avicola

    def delete(self, id):
        removido = self.avicola_repository.delete(id)
        logger.info(f"Avicola {id} removida: {removido}")
        return removido