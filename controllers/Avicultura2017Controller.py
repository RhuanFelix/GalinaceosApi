from flask import Blueprint, request, jsonify
from services.Avicultura2017Service import Avicultura2017Service

galinaceos_bp = Blueprint('galinaceos', __name__, url_prefix='/galinaceos')
service = Avicultura2017Service()

@galinaceos_bp.get("/")
def get_galinaceos():

    try:
        filters = {}
        
        if request.args.get('sist_cria'):
            filters['sist_cria'] = request.args.get('sist_cria')
        
        if request.args.get('niv_terr'):
            filters['niv_terr'] = request.args.get('niv_terr')
        
        if request.args.get('cod_terr'):
            filters['cod_terr'] = request.args.get('cod_terr')
        
        if request.args.get('nom_terr'):
            filters['nom_terr'] = request.args.get('nom_terr')
        
        if request.args.get('cl_gal'):
            filters['cl_gal'] = request.args.get('cl_gal')
        
        aviculturas = service.get_by_filters(filters)
        
        resultado = [av.toDict() for av in aviculturas]
        
        return jsonify({
            'total': len(resultado),
            'dados': resultado
        }), 200
    
    except ValueError as e:
        return jsonify({
            'erro': 'Parâmetros inválidos',
            'detalhes': str(e)
        }), 400
    
    except Exception as e:
        return jsonify({
            'erro': 'Erro ao buscar dados',
            'detalhes': str(e)
        }), 500

