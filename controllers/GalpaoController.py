from flask import request, jsonify
from flask_restful import Resource, marshal
from marshmallow import ValidationError

from helpers.logger import logger
from models.Galpao import galpao_fields, GalpaoSchema
from services.GalpaoService import GalpaoService

CAMPOS_FILTRO = {'codigo', 'area_m2'}

class GalpoesController(Resource):
    def get(self):
        logger.info("Listando todos os galpoes")
        filtros = {k: v for k, v in request.args.items() if k in CAMPOS_FILTRO and v}
        galpoes = GalpaoService().get_all(filtros)
        return marshal(galpoes, galpao_fields), 200

    def post(self):
        try:
            data = GalpaoSchema().load(request.get_json())
            galpao = GalpaoService().create(data)
            return marshal(galpao, galpao_fields), 201
        except ValidationError as err:
            return jsonify(err.messages), 400

class GalpaoController(Resource):
    def get(self, id):
        logger.info(f"Listando galpao pelo id: {id}")
        galpao = GalpaoService().get_by_id(id)
        if galpao is None:
            return {'mensagem': 'O galpao não foi encontrado.'}, 404
        return marshal(galpao, galpao_fields), 200

    def put(self, id):
        try:
            data = GalpaoSchema().load(request.get_json())
            galpao = GalpaoService().update(id, data)
            if galpao is None:
                return {'mensagem': 'O galpao não foi encontrado.'}, 404
            return marshal(galpao, galpao_fields), 200
        except ValidationError as err:
            return jsonify(err.messages), 400

    def delete(self, id):
        logger.info(f"Removendo galpao id: {id}")
        removido = GalpaoService().delete(id)
        if not removido:
            return {'mensagem': 'O galpao não foi encontradao'}, 404
        return {'mensagem': 'Galpao removida com sucesso!'}, 200