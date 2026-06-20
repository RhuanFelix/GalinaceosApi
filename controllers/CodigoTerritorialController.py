from flask import Blueprint, jsonify, request
from marshmallow import ValidationError
from models.CodigoTerritorial import CodigoTerritorialSchema
from services.CodigoTerritorialService import CodigoTerritorialService

codigo_territorial_bp = Blueprint('codigoterritorial', __name__, url_prefix='/codigoterritorial')

@codigo_territorial_bp.get("/<int:id>")
def getById(id):
    codigoTerritorial = CodigoTerritorialService().getById(id)
    if codigoTerritorial is None:
        return {"mensagem": "Código territorial não encontrado"}, 404
    return codigoTerritorial.toDict()

@codigo_territorial_bp.get("/")
def getAll():
    codigosTerritoriais = CodigoTerritorialService().getAll()
    return [ct.toDict() for ct in codigosTerritoriais], 200

@codigo_territorial_bp.post("/")
def create():
    try:
        data = CodigoTerritorialSchema().load(request.get_json())
        codigoTerritorial = CodigoTerritorialService().create(data)
        return codigoTerritorial.toDict(), 201
    except ValidationError as err:
        return jsonify(err.messages), 400

@codigo_territorial_bp.put("/<int:id>")
def update(id):
    try:
        data = CodigoTerritorialSchema().load(request.get_json())
        codigoTerritorial = CodigoTerritorialService().update(id, data)
        if codigoTerritorial is None:
            return {"mensagem": "Código territorial não encontrado"}, 404
        return codigoTerritorial.toDict(), 200
    except ValidationError as err:
        return jsonify(err.messages), 400

@codigo_territorial_bp.delete("/<int:id>")
def delete(id):
    removido = CodigoTerritorialService().delete(id)
    if not removido:
        return {"mensagem": "Código territorial não encontrado"}, 404
    return {"mensagem": "Código territorial removido com sucesso!"}, 200