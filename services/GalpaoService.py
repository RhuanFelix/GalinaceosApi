from helpers.logger import logger
from repositories.GalpaoRepository import GalpaoRepository


class GalpaoService:
    def __init__(self):
        self.galpao_repository = GalpaoRepository()

    def get_all(self, filtros: dict = None):
        galpoes = self.galpao_repository.get_all(filtros)
        logger.info(f"Retornando {len(galpoes)} galpoes.")
        return galpoes

    def get_by_id(self, id):
        galpao = self.galpao_repository.get_by_id(id)
        logger.info("Lendo informações do resultado da consulta ao banco")
        return galpao

    def create(self, data):
        galpao = self.galpao_repository.insert(data['codigo'], data['area_m2'], data['aviario_id'])
        logger.info(f"Galpão criado com id: {galpao.id}")
        return galpao

    def update(self, id, data):
        galpao = self.galpao_repository.update(id, data['codigo'], data['area_m2'], data['aviario_id'])
        if galpao is None:
            return None
        logger.info(f"Galpão atualizado com id: {id}")
        return galpao

    def delete(self, id):
        removido = self.galpao_repository.delete(id)
        logger.info(f"Galpao {id} removido: {removido}")
        return removido