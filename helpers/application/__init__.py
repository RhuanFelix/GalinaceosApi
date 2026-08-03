from dotenv import load_dotenv
from flask import Flask
from flask_restful import Api

from helpers.cors import cors
from helpers.enviroment import enviroment

app = Flask(__name__)

load_dotenv()

DATABASE_NAME = enviroment.get("DB_NAME")
DATABASE_USER = enviroment.get("DB_USER")
DATABASE_PASSWORD = enviroment.get("DB_PASSWORD")
DATABASE_PORT = enviroment.get("DB_PORT")
DATABASE_HOST = enviroment.get("DB_HOST")

app.config['SQLALCHEMY_DATABASE_URI'] = f'postgresql://{DATABASE_USER}:{DATABASE_PASSWORD}@{DATABASE_HOST}:{DATABASE_PORT}/{DATABASE_NAME}'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

api = Api(app)
cors.init_app(app)