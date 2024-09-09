import pandas as pd

import streamlit as st

st.title("App Rodando em Ambiente Virtual")
st.write("Este aplicativo está rodando em um ambiente virtual com Streamlit!")

nome = st.text_input("Digite seu nome:")
if st.button("Enviar"):
    st.write(f"Olá, {nome}!")
    