from flask import g
import psycopg2

import app
from helpers.environment import environment


DATABASE_NAME = environment.get("DB_NAME")
DATABASE_USER = environment.get("DB_USER")
DATABASE_PASS = environment.get("DB_PASSWORD")
DATABASE_PORT = environment.get("DB_PORT")
DATABASE_HOST = environment.get("DB_HOST")

def get_conn():
    conn = getattr(g, '_database', None)
    if conn is None:
        conn = g._database = psycopg2.connect(
            database=DATABASE_NAME, user=DATABASE_USER, password=DATABASE_PASS, host=DATABASE_HOST, port=DATABASE_PORT)
    return conn

@app.teardown_appcontext
def close_connection(exception):
    conn = getattr(g, '_database', None)
    if conn is not None:
        conn.close()