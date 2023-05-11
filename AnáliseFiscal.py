import streamlit as st
from notas_fiscais import notas_fiscais


def main():
# Configuração do layout
st.set_page_config(page_title="Aplicativo de Análise Fiscal")

# Título do aplicativo
st.title("Aplicativo de Análise Fiscal")

# Criação das guias na barra lateral
opcao = st.sidebar.selectbox("Selecione uma opção","Notas Fiscais")

 if notasfiscais_choice == "Notas Fiscais":
            notas_fiscais()

