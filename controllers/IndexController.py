from flask_restful import Resource
from sqlalchemy import text

from helpers.database import db


class IndexController(Resource):
    def get(self):
        return {'versão': '1.0.0'}, 200

class HealthController(Resource):
    def get(self):
        try:
            db.session.execute(text("SELECT 1;"))
            return {'status': 'healthy', 'message': 'Database verified.'}
        except Exception as e:
            return {'status': 'unhealthy', 'message': f'Unexpected error: {e}'}