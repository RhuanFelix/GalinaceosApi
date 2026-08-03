from helpers.logger import logger
from repositories.GalinaceosRepository import GalinaceosRepository


class GalinaceosService:
    def __init__(self):
        self.galinaceos_repository = GalinaceosRepository()

    def get_all(self, filtros: dict = None):
        galinaceos = self.galinaceos_repository.get_all()
        logger.info(f"Retornando {len(galinaceos)} Galinaceos")
        return galinaceos