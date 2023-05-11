import streamlit as st

def notas_fiscais_complementar():
    st.write("Conteúdo da guia Notas Fiscais + Complementar")

def efd():
    st.write("Conteúdo da guia EFD")

def cat():
    st.write("Conteúdo da guia CAT")

def analise_fiscal():
    st.write("Conteúdo da guia Análise Fiscal")

# Configuração das guias
tabs = {
    "Notas Fiscais + Complementar": notas_fiscais_complementar,
    "EFD": efd,
    "CAT": cat,
    "Análise Fiscal": analise_fiscal
}

# Configuração do layout
st.set_page_config(page_title="Aplicativo de Análise Fiscal")

# Título do aplicativo
st.title("Aplicativo de Análise Fiscal")

# Criação das guias na barra lateral
tab = st.sidebar.radio("Selecione uma guia", tuple(tabs.keys()))
tabs[tab]()  # Chama a função correspondente à guia selecionada
