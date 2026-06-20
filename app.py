from helpers.application import app

@app.get("/")
def index():
    return "{'versão':'0.1.1'}", 200

@app.get("/health")
def healthCheck():
    return "{'online':'true'}", 200