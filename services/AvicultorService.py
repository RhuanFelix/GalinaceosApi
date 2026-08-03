from helpers.logger import logger
from repositories.AvicultorRepository import AvicultorRepository


class AvicultorService:
    def __init__(self):
        self.avicultor_repository = AvicultorRepository()

    def get_all(self, filtros: dict = None):
        avicultores = self.avicultor_repository.get_all(filtros)
        logger.info(f"Retornando {len(avicultores)} avicultores.")
        return avicultores

    def get_by_id(self, id):
        avicultor = self.avicultor_repository.get_by_id(id)
        logger.info("Lendo informações do resultado da consulta ao banco")
        return avicultor

    def create(self, data):
        avicultor = self.avicultor_repository.insert(data['nome'], data['nascimento'], data['cpf'], data['caf'], data['avicola_id'])
        logger.info(f"Avicultor criado com id: {avicultor.id}")
        return avicultor

    def update(self, id, data):
        avicultor = self.avicultor_repository.update(id, data['nome'], data['nascimento'], data['cpf'], data['caf'], data['avicola_id'])
        if avicultor is None:
            return None
        logger.info(f"Avicultor atualizado com id: {id}")
        return avicultor

    def delete(self, id):
        removido = self.avicultor_repository.delete(id)
        logger.info(f"Avicultor {id} removido: {removido}")
        return removido