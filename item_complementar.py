import streamlit as st
import pandas as pd


def item_complementar(file):
    def read_xlsx(file):
        return pd.read_excel(file)

    st.title("Leitor de Arquivos Excel")

    uploaded_file = st.file_uploader("Selecione o arquivo Excel:", type=["xlsx"])

    if uploaded_file is not None:
        df = read_xlsx(uploaded_file)
        st.write(df)
        

