import psycopg2
from helpers.environment import environment
from helpers.logger import logger

DATABASE_NAME = environment.get("DB_NAME")
DATABASE_USER = environment.get("DB_USER")
DATABASE_PASS = environment.get("DB_PASSWORD")
DATABASE_PORT = environment.get("DB_PORT")
DATABASE_HOST = environment.get("DB_HOST")

conn = None
try:
    conn = psycopg2.connect(database=DATABASE_NAME, user=DATABASE_USER, password=DATABASE_PASS, host=DATABASE_HOST, port=DATABASE_PORT)
    logger.info("Conectou ao banco de dados")
    cursor = conn.cursor()
    with open('schema.sql', mode='r') as file:
        cursor.execute(file.read())
    logger.info("Criou as tabelas")
    conn.commit()
except psycopg2.Error as e:
    logger.error(e)
finally:
    if conn:
        conn.close()