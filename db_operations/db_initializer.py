from db_operations.db_connector import connect_to_db, close_connection
from utils.sql_queries import create_table_query, insert_records_query

def create_table():
    """
    Creates the specified table in the database.

    1. Establishes a connection to the database.
    2. Executes the provided SQL query to create the table.
    3. Commits the changes to the database.
    4. Handles potential errors and closes the connection gracefully.

    Note: The SQL query for creating the table should be defined in the
    `create_table_query` variable.

    Raises:
        Exception: If there is an error during table creation.
    """
    conn, mycursor = connect_to_db()
    # Check if the connection is successful
    if conn:
        try:
            # Execute the SQL query to create the table
            mycursor.execute(create_table_query)
            # Commit the changes to the database
            conn.commit()
            print("Table created Successfully")
        except Exception as e:
            print("Error in creating the table")
            print(e)
        finally:
            # Close the database connection
            close_connection(conn)

def insert_records():
    """
    Inserts records into the specified table in the database.

    1. Establishes a connection to the database.
    2. Executes the provided SQL query to insert records.
    3. Commits the changes to the database.
    4. Handles potential errors and closes the connection gracefully.

    Note: The SQL query for inserting records should be defined in the
    `insert_records_query` variable.

    Raises:
        Exception: If there is an error during record insertion.
    """
    conn, mycursor = connect_to_db()
    # Check if the connection is successful
    if conn:
        try:
            # Execute the SQL query to insert records into the table
            mycursor.execute(insert_records_query)
            # Commit the changes to the database
            conn.commit()
            print("records inserted Successfully")
        except Exception as e:
            print("Error in inserting the records")
            print(e)
        finally:
            # Close the database connection
            close_connection(conn)