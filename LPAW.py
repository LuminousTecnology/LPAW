import pandas as pd

import streamlit as st

st.title("App de teste")
st.write("Ola leandro bundao, estou testando pra ver se funciona")

nome = st.text_input("Digite seu nome:")
if st.button("Enviar"):
    st.write(f"Olá, {nome}!")
    