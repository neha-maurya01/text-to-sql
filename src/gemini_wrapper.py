from configuration.config import load_api_key
import google.generativeai as genai
from db_operations.db_connector import connect_to_db

def configure_gemini():
    genai.configure(api_key=load_api_key())

def get_response_as_sql_query(user_prompt, system_prompt):
    model = genai.GenerativeModel("gemini-pro")
    response = model.generate_content([system_prompt[0], user_prompt])
    return response.text

def get_query_response_as_text(sql_query):
    conn, mycursor = connect_to_db()
    mycursor.execute(sql_query)
    rows = mycursor.fetchall()
    conn.commit()
    conn.close()
    for row in rows:
        print(row)
    return rows