from helpers.application import app
from controllers.SistemaCriacaoController import sistema_criacao_bp
from controllers.NivelTerritorialController import nivel_territorial_bp
from controllers.CodigoTerritorialController import codigo_territorial_bp

@app.get("/")
def index():
    return "{'versão':'0.5.0'}", 200

@app.get("/health")
def healthCheck():
    return "{'online':'true'}", 200

app.register_blueprint(sistema_criacao_bp)
app.register_blueprint(nivel_territorial_bp)
app.register_blueprint(codigo_territorial_bp)