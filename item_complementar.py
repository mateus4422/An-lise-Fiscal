import streamlit as st
import pandas as pd

def item_complementar():
    def read_xlsx(file):
        df = pd.read_excel(file)
        # Garante que os dados da coluna 2 estão no formato correto
        df[df.columns[2]] = df[df.columns[2]].replace(',', '', regex=True).astype(int)
        return df

    st.title("Leitor de Arquivos Excel")

    uploaded_file = st.file_uploader("Selecione o arquivo Excel:", type=["xlsx"], key="item_complementar")

    if uploaded_file is not None:
        df = read_xlsx(uploaded_file)
        st.write(df)

item_complementar()
