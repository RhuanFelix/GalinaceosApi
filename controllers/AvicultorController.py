from flask import request, jsonify
from flask_restful import Resource, marshal
from marshmallow import ValidationError

from helpers.logger import logger
from models.Avicultor import avicultor_fields, AvicultorSchema
from services.AvicultorService import AvicultorService

CAMPOS_FILTRO = {'nome', 'cpf', 'caf'}

class AvicultoresController(Resource):
    def get(self):
        logger.info("Listando todos as avicultores")
        filtros = {k: v for k, v in request.args.items() if k in CAMPOS_FILTRO and v}
        avicultores = AvicultorService().get_all(filtros)
        return marshal(avicultores, avicultor_fields), 200

    def post(self):
        try:
            data = AvicultorSchema().load(request.get_json())
            avicultor = AvicultorService().create(data)
            return marshal(avicultor, avicultor_fields), 201
        except ValidationError as err:
            return jsonify(err.messages), 400

class AvicultorController(Resource):
    def get(self, id):
        logger.info(f"Listando avicultor pelo id: {id}")
        avicultor = AvicultorService().get_by_id(id)
        if avicultor is None:
            return {'mensagem': 'O avicultor não foi encontrado.'}, 404
        return marshal(avicultor, avicultor_fields), 200

    def put(self, id):
        try:
            data = AvicultorSchema().load(request.get_json())
            avicultor = AvicultorService().update(id, data)
            if avicultor is None:
                return {'mensagem': 'O avicultor não foi encontrado.'}, 404
            return marshal(avicultor, avicultor_fields), 200
        except ValidationError as err:
            return jsonify(err.messages), 400

    def delete(self, id):
        logger.info(f"Removendo avicultor id: {id}")
        removido = AvicultorService().delete(id)
        if not removido:
            return {'mensagem': 'O avicultor não foi encontrado'}, 404
        return {'mensagem': 'Avicultor removido com sucesso!'}, 200