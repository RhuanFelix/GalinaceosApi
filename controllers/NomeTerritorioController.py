from flask import Blueprint, jsonify, request
from marshmallow import ValidationError
import psycopg2
from helpers.logger import logger
from models.NomeTerritorio import NomeTerritorioSchema
from services.NomeTerritorioService import NomeTerritorioService

nome_territorio_bp = Blueprint('nometerritorio', __name__, url_prefix='/nometerritorio')

@nome_territorio_bp.get("/<int:id>")
def getById(id):
    nomeTerritorio = NomeTerritorioService().getById(id)
    if nomeTerritorio is None:
        return {"mensagem": "Nome do território não encontrado"}, 404
    return nomeTerritorio.toDict()

@nome_territorio_bp.get("/")
def getAll():
    nomesTerritorios = NomeTerritorioService().getAll()
    return [nt.toDict() for nt in nomesTerritorios], 200

@nome_territorio_bp.post("/")
def create():
    try:
        data = NomeTerritorioSchema().load(request.get_json())
        nomeTerritorio = NomeTerritorioService().create(data)
        return nomeTerritorio.toDict(), 201
    except psycopg2.Error as err:
        logger.error(err)
    except ValidationError as err:
        return jsonify(err.messages), 400

@nome_territorio_bp.put("/<int:id>")
def update(id):
    try:
        data = NomeTerritorioSchema().load(request.get_json())
        nomeTerritorio = NomeTerritorioService().update(id, data)
        if nomeTerritorio is None:
            return {"mensagem": "Nome do território não encontrado"}, 404
        return nomeTerritorio.toDict(), 200
    except ValidationError as err:
        return jsonify(err.messages), 400

@nome_territorio_bp.delete("/<int:id>")
def delete(id):
    removido = NomeTerritorioService().delete(id)
    if not removido:
        return {"mensagem": "Nome do território não encontrado"}, 404
    return {"mensagem": "Nome do território removido com sucesso!"}, 200