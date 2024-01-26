import streamlit as st
import sqlalchemy
from langchain_helper import get_few_shot_db_chain,llm

st.title("Retail Store T-Shirts: Database Q&A 👕")

question = st.text_input("Question: ")

if question:
    chain = get_few_shot_db_chain()

    try:
        response = f"LLM Response from database: {chain.run(question)}"
    except Exception as e:
        # Handle the exception, e.g., print an error message
        # print(f"Error: {e}")

        # Use the language model (llm) to generate a response
        llm_response = llm(question)
        response = f"LLM Response: {llm_response}"
    print(response)


    st.header("Answer")
    st.write(response)






