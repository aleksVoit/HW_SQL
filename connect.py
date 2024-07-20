import sqlite3
from contextlib import contextmanager
import psycopg2

# database = './test.db'

# @contextmanager
# def create_connection(db_file):
    # conn = sqlite3.connect(db_file)
    # yield conn
    # conn.rollback()
    # conn.close()

connection = psycopg2.connect(
        dbname='hw_6',
        user='postgres',
        password='0000',
        host='localhost',
        port='5432'
    )