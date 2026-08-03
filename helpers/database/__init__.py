from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import DeclarativeBase

from helpers.application import app


class Base(DeclarativeBase):
    pass

db = SQLAlchemy(model_class=Base)
db.init_app(app)