import streamlit as st
import requests

API_URL = "http://localhost:8000/ask"

st.title(" RAG BAF Assistant")

question = st.text_input("Haz tu pregunta:")

if st.button("Enviar"):
    if question:
        response = requests.post(API_URL, json={"question": question})
        answer = response.json()["answer"]

        st.write("### Respuesta:")
        st.write(answer)