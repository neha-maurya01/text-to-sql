from src.gemini_wrapper import get_response_as_sql_query, get_query_response_as_text, configure_gemini
from utils.prompts import system_prompt
import streamlit as st

configure_gemini()
# a = get_response_as_sql_query(user_prompt="how many total student are there",system_prompt=system_prompt)
# print(a)
# print(get_query_response_as_text(a))

st.set_page_config(page_title="Text to SQL query Generator")
st.header("Database Retriever")
question = st.text_input("Input: ", key="input")
submit = st.button("Ask the question")

if submit:
    response_sql = get_response_as_sql_query(question,system_prompt)
    data = get_query_response_as_text(response_sql)
    st.subheader("The response is: ")
    for row in data:
        print(row)
        st.write(row)
