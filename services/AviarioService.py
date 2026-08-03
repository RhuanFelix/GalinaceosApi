from helpers.logger import logger
from repositories.AviarioRepository import AviarioRepository


class AviarioService:
    def __init__(self):
        self.aviario_repository = AviarioRepository()

    def get_all(self, filtros: dict = None):
        aviarios = self.aviario_repository.get_all(filtros)
        logger.info(f"Retornando {len(aviarios)} aviarios.")
        return aviarios

    def get_by_id(self, id):
        aviario = self.aviario_repository.get_by_id(id)
        logger.info("Lendo informações do resultado da consulta ao banco")
        return aviario

    def create(self, data):
        aviario = self.aviario_repository.insert(data['nome'], data['capacidade'], data['tipo'], data['avicola_id'])
        logger.info(f"Aviario criada com id: {aviario.id}")
        return aviario

    def update(self, id, data):
        aviario = self.aviario_repository.update(id, data['nome'], data['capacidade'], data['tipo'], data['avicola_id'])
        if aviario is None:
            return None
        logger.info(f"Aviario atualizada com id: {id}")
        return aviario

    def delete(self, id):
        removido = self.aviario_repository.delete(id)
        logger.info(f"Aviario {id} removida: {removido}")
        return removido