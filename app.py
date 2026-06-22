from helpers.application import app
from controllers.SistemaCriacaoController import sistema_criacao_bp
from controllers.NivelTerritorialController import nivel_territorial_bp
from controllers.CodigoTerritorialController import codigo_territorial_bp
from controllers.NomeTerritorioController import nome_territorio_bp
from controllers.ClasseCabecaGalinaceos import classe_cabeca_bp
from controllers.Avicultura2017Controller import galinaceos_bp

@app.get("/")
def index():
    return "{'versão':'0.8.0'}", 200

@app.get("/health")
def healthCheck():
    return "{'online':'true'}", 200


app.register_blueprint(sistema_criacao_bp)
app.register_blueprint(nivel_territorial_bp)
app.register_blueprint(codigo_territorial_bp)
app.register_blueprint(nome_territorio_bp)
app.register_blueprint(classe_cabeca_bp)
app.register_blueprint(galinaceos_bp)