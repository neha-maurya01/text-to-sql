from db_operations.db_connector import connect_to_db, close_connection
from utils.sql_queries import create_table_query, insert_records_query

def create_table():
    conn, mycursor = connect_to_db()
    if conn:
        try:
            mycursor.execute(create_table_query)
            conn.commit()
            print("Table created Successfully")
        except Exception as e:
            print("Error in creating the table")
            print(e)
        finally:
            close_connection(conn)

def insert_records():
    conn, mycursor = connect_to_db()
    if conn:
        try:
            mycursor.execute(insert_records_query)
            conn.commit()
            print("records inserted Successfully")
        except Exception as e:
            print("Error in inserting the records")
            print(e)
        finally:
            close_connection(conn)