from flask import Blueprint, jsonify, request
from marshmallow import ValidationError

from models.SistemaCriacao import SistemaCriacaoSchema
from services.SistemaCriacaoService import SistemaCriacaoService


sistema_criacao_bp = Blueprint('sistemacriacao', __name__, url_prefix='/sistemacriacao')

@sistema_criacao_bp.get("/<int:id>")
def getByIdSistemaCriacao(id: int):
    sistemaCriacao = SistemaCriacaoService().getById(id)
    if sistemaCriacao is None:
        return {"mensagem":"O sistema de criação não foi encontrado"}, 404
    return sistemaCriacao.toDict()

@sistema_criacao_bp.get("/")
def getSistemasCriacoes():
    sistemaCriacao = SistemaCriacaoService().getAll()
    return [sc.toDict() for sc in sistemaCriacao], 200

@sistema_criacao_bp.post("/")
def postAvicultores():
    try:
        data = SistemaCriacaoSchema().load(request.get_json())
        avicultor = SistemaCriacaoService().create(data)
        return avicultor.toDict(), 201
    except ValidationError as err:
        return jsonify(err.messages), 400
    
@sistema_criacao_bp.put("/<int:id>")
def putAvicultores(id: int):
    try:
        data = SistemaCriacaoSchema().load(request.get_json())
        avicultor = SistemaCriacaoService().update(id, data)
        if avicultor is None:
            return {"mensagem": "O sistema de criação não foi encontrado"}, 404
        return avicultor.toDict(), 200
    except ValidationError as err:
        return jsonify(err.messages), 400
    
@sistema_criacao_bp.delete("/<int:id>")
def deleteAvicultores(id: int):
    removido = SistemaCriacaoService().delete(id)
    if not removido:
        return {"mensagem": "O sistema de criação não foi encontrado"}, 404
    return {"mensagem": "Sistema de criação removido com sucesso!"}, 200