from configuration.config import load_api_key
import google.generativeai as genai
from db_operations.db_connector import connect_to_db

def configure_gemini():
    """
    Initializes the Gemini generative model with the appropriate API key.

    1. Retrieves the API key securely from the environment variables.
    2. Configures the generativeai library with the retrieved API key.

    Raises:
        ValueError: If the API key is not available.
    """
    genai.configure(api_key=load_api_key())

def get_response_as_sql_query(user_prompt, system_prompt):
    """
    Generates an SQL query based on user and system prompts using Gemini.

    1. Leverages the Gemini generative model to create an SQL query.
    2. Takes both user_prompt and system_prompt as input for context.
    3. Returns the generated SQL query as text.
    """
    # Load Gemini model
    model = genai.GenerativeModel("gemini-pro")
    # Generate the sql queries using the model and provided prompts
    response = model.generate_content([system_prompt[0], user_prompt])
    # Return the generated sql query
    return response.text

def get_query_response_as_text(sql_query):
    """
    Executes a SQL query and retrieves the response from the database.

    This function establishes a connection to the database using the
    `connect_to_db` function. It then executes the provided SQL query,
    fetches the results, and returns them.

    Parameters:
        sql_query (str): The SQL query to be executed.

    Returns:
        list: The result rows obtained from executing the SQL query.
    """
    # Establish a connection to the database
    conn, mycursor = connect_to_db()
    # Execute the provided SQL query
    mycursor.execute(sql_query)
    # Fetch the results and close the connection
    rows = mycursor.fetchall()
    conn.commit()
    conn.close()
    # Return the result rows
    return rows