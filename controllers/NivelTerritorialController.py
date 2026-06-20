from flask import Blueprint, jsonify, request
from marshmallow import ValidationError
from models.NivelTerritorial import NivelTerritorialSchema
from services.NivelTerritorialService import NivelTerritorialService

nivel_territorial_bp = Blueprint('nivelterritorial', __name__, url_prefix='/nivelterritorial')

@nivel_territorial_bp.get("/<int:id>")
def getById(id):
    nivelTerritorial = NivelTerritorialService().getById(id)
    if nivelTerritorial is None:
        return {"mensagem": "Nível territorial não encontrado"}, 404
    return nivelTerritorial.toDict()

@nivel_territorial_bp.get("/")
def getAll():
    niveisTerritoriais = NivelTerritorialService().getAll()
    return [nt.toDict() for nt in niveisTerritoriais], 200

@nivel_territorial_bp.post("/")
def create():
    try:
        data = NivelTerritorialSchema().load(request.get_json())
        nivelTerritorial = NivelTerritorialService().create(data)
        return nivelTerritorial.toDict(), 201
    except ValidationError as err:
        return jsonify(err.messages), 400

@nivel_territorial_bp.put("/<int:id>")
def update(id):
    try:
        data = NivelTerritorialSchema().load(request.get_json())
        nivelTerritorial = NivelTerritorialService().update(id, data)
        if nivelTerritorial is None:
            return {"mensagem": "Nível territorial não encontrado"}, 404
        return nivelTerritorial.toDict(), 200
    except ValidationError as err:
        return jsonify(err.messages), 400

@nivel_territorial_bp.delete("/<int:id>")
def delete(id):
    removido = NivelTerritorialService().delete(id)
    if not removido:
        return {"mensagem": "Nível territorial não encontrado"}, 404
    return {"mensagem": "Nível territorial removido com sucesso!"}, 200