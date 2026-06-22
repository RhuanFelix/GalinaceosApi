from flask import Blueprint, jsonify, request
from marshmallow import ValidationError
from models.ClasseCabecaGalinaceos import ClasseCabecaGalinaceosSchema
from services.ClasseCabecaGalinaceosService import ClasseCabecaGalinaceosService

classe_cabeca_bp = Blueprint('classecabecagalinaceos', __name__, url_prefix='/classecabecagalinaceos')

@classe_cabeca_bp.get("/<int:id>")
def getById(id):
    classeCabecaGalinaceo = ClasseCabecaGalinaceosService().getById(id)
    if classeCabecaGalinaceo is None:
        return {"mensagem": "Classe cabeça galináceos não encontrada"}, 404
    return classeCabecaGalinaceo.toDict()

@classe_cabeca_bp.get("/")
def getAll():
    classeCabecaGalinaceos = ClasseCabecaGalinaceosService().getAll()
    return [o.toDict() for o in classeCabecaGalinaceos], 200

@classe_cabeca_bp.post("/")
def create():
    try:
        data = ClasseCabecaGalinaceosSchema().load(request.get_json())
        classeCabecaGalinaceo = ClasseCabecaGalinaceosService().create(data)
        return classeCabecaGalinaceo.toDict(), 201
    except ValidationError as err:
        return jsonify(err.messages), 400

@classe_cabeca_bp.put("/<int:id>")
def update(id):
    try:
        data = ClasseCabecaGalinaceosSchema().load(request.get_json())
        classeCabecaGalinaceo = ClasseCabecaGalinaceosService().update(id, data)
        if classeCabecaGalinaceo is None:
            return {"mensagem": "Classe cabeça galináceos não encontrada"}, 404
        return classeCabecaGalinaceo.toDict(), 200
    except ValidationError as err:
        return jsonify(err.messages), 400

@classe_cabeca_bp.delete("/<int:id>")
def delete(id):
    removido = ClasseCabecaGalinaceosService().delete(id)
    if not removido:
        return {"mensagem": "Classe cabeça galináceos não encontrada"}, 404
    return {"mensagem": "Classe cabeça galináceos removida com sucesso!"}, 200