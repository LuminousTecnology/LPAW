import pandas as pd

import streamlit as st

st.title("App de teste")
st.write("Quem joga pubg e muito gay")

nome = st.text_input("Digite seu nome:")
if st.button("Enviar"):
    st.write(f"Olá, {nome}!")
    