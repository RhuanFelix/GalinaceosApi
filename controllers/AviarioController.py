from flask import request, jsonify
from flask_restful import Resource, marshal
from marshmallow import ValidationError

from helpers.logger import logger
from models.Aviario import aviario_fields, AviarioSchema
from services.AviarioService import AviarioService

CAMPOS_FILTRO = {'nome', 'capacidade', 'tipo'}

class AviariosController(Resource):
    def get(self):
        logger.info("Listando todos os aviarios")
        filtros = {k: v for k, v in request.args.items() if k in CAMPOS_FILTRO and v}
        aviarios = AviarioService().get_all(filtros)
        return marshal(aviarios, aviario_fields), 200

    def post(self):
        try:
            data = AviarioSchema().load(request.get_json())
            aviario = AviarioService().create(data)
            return marshal(aviario, aviario_fields), 201
        except ValidationError as err:
            return jsonify(err.messages), 400

class AviarioController(Resource):
    def get(self, id):
        logger.info(f"Listando aviario pelo id: {id}")
        aviario = AviarioService().get_by_id(id)
        if aviario is None:
            return {'mensagem': 'O aviario não foi encontrado.'}, 404
        return marshal(aviario, aviario_fields), 200

    def put(self, id):
        try:
            data = AviarioSchema().load(request.get_json())
            aviario = AviarioService().update(id, data)
            if aviario is None:
                return {'mensagem': 'O aviario não foi encontrado.'}, 404
            return marshal(aviario, aviario_fields), 200
        except ValidationError as err:
            return jsonify(err.messages), 400

    def delete(self, id):
        logger.info(f"Removendo aviario id: {id}")
        removido = AviarioService().delete(id)
        if not removido:
            return {'mensagem': 'O aviario não foi encontradao'}, 404
        return {'mensagem': 'Aviario removida com sucesso!'}, 200