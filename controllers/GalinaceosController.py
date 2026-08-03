from flask import request
from flask_restful import Resource, marshal

from helpers.logger import logger
from models.Galinaceos import galinaceos_fields
from services.GalinaceosService import GalinaceosService

CAMPOS_FILTRO = {'SIST_CRIA', 'NIV_TERR', 'COD_TERR', 'NOM_TERR', 'CL_GAL'}

class GalinaceosController(Resource):
    def get(self):
        logger.info(f"Listando todos os Galinaceos")
        filtros = {k: v for k, v in request.args.items() if k in CAMPOS_FILTRO and v}
        galinaceos = GalinaceosService().get_all(filtros)
        return marshal(galinaceos, galinaceos_fields), 200