import mysql.connector
import os
from dotenv import load_dotenv
from constants import constant

load_dotenv()

def connect_to_db():
    """
    Establishes a connection to the MySQL database.

    Attempts to connect to the database using the specified host, user,
    password, and database name. If successful, it returns the database
    connection and cursor objects.

    Returns:
       tuple: (connection object, cursor object) if successful,
              None if an error occurs
   """
    try:
        # Create a connection to the MySQL database
        conn = mysql.connector.connect(
            host=constant.DB_HOST,
            user=os.environ.get("DB_USER"),
            password=os.environ.get("DB_PASSWORD"),
            database=constant.DB_NAME
        )
       # Create a cursor object for executing queries
        cur = conn.cursor()
        return conn, cur
    except Exception as e:
        # Print an error message if the connection fails
        print("Connection Error")
        print(e)
        return None

def close_connection(conn):
    """
   Closes the specified database connection.

   Checks if the connection object is valid and, if so, closes it.
   """
    if conn:
        conn.close()
