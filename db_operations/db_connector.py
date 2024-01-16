import mysql.connector
import os
from dotenv import load_dotenv
from constants import constant

load_dotenv()

def connect_to_db():
    try:
        conn = mysql.connector.connect(
            host=constant.DB_HOST,
            user=os.environ.get("DB_USER"),
            password=os.environ.get("DB_PASSWORD"),
            database=constant.DB_NAME
        )
        cur = conn.cursor()
        return conn, cur
    except Exception as e:
        print("Connection Error")
        print(e)
        return None

def close_connection(conn):
    if conn:
        conn.close()
