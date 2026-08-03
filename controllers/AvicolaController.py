from flask import request, jsonify
from flask_restful import Resource, marshal
from marshmallow import ValidationError

from helpers.logger import logger
from models.Avicola import avicola_fields, AvicolaSchema
from services.AvicolaService import AvicolaService

CAMPOS_FILTRO = {'nome', 'endereco', 'telefone'}

class AvicolasController(Resource):
    def get(self):
        logger.info("Listando todos as avicolas")
        filtros = {k: v for k, v in request.args.items() if k in CAMPOS_FILTRO and v}
        avicolas = AvicolaService().get_all(filtros)
        return marshal(avicolas, avicola_fields), 200

    def post(self):
        try:
            data = AvicolaSchema().load(request.get_json())
            avicola = AvicolaService().create(data)
            return marshal(avicola, avicola_fields), 201
        except ValidationError as err:
            return jsonify(err.messages), 400

class AvicolaController(Resource):
    def get(self, id):
        logger.info(f"Listando avicola pelo id: {id}")
        avicola = AvicolaService().get_by_id(id)
        if avicola is None:
            return {'mensagem': 'A avicola não foi encontrada.'}, 404
        return marshal(avicola, avicola_fields), 200

    def put(self, id):
        try:
            data = AvicolaSchema().load(request.get_json())
            avicola = AvicolaService().update(id, data)
            if avicola is None:
                return {'mensagem': 'A avicola não foi encontrada.'}, 404
            return marshal(avicola, avicola_fields), 200
        except ValidationError as err:
            return jsonify(err.messages), 400

    def delete(self, id):
        logger.info(f"Removendo avicola id: {id}")
        removido = AvicolaService().delete(id)
        if not removido:
            return {'mensagem': 'A avicola não foi encontrada'}, 404
        return {'mensagem': 'Avicola removida com sucesso!'}, 200