from controllers.AviarioController import AviariosController, AviarioController
from controllers.AvicolaController import AvicolasController, AvicolaController
from controllers.AvicultorController import AvicultorController, AvicultoresController
from controllers.GalinaceosController import GalinaceosController
from controllers.GalpaoController import GalpaoController, GalpoesController
from controllers.IndexController import IndexController, HealthController
from helpers.application import api, app
from helpers.database import db

api.add_resource(IndexController, '/')
api.add_resource(HealthController, '/health')

api.add_resource(AvicolasController, '/avicolas')
api.add_resource(AvicolaController, '/avicola/<int:id>')

api.add_resource(AvicultoresController, '/avicultores')
api.add_resource(AvicultorController, '/avicultor/<int:id>')

api.add_resource(AviariosController, '/aviarios')
api.add_resource(AviarioController, '/aviario/<int:id>')

api.add_resource(GalpoesController, '/galpoes')
api.add_resource(GalpaoController, '/galpao')

api.add_resource(GalinaceosController, '/galinaceos')

with app.app_context():
    db.create_all()