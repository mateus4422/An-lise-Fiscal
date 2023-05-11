import streamlit as st
from notas_fiscais import notas_fiscais


def main():
 menu_options = ["Notas Fiscais", "Notas Complementares", "EFD",  "CAT"]
    choice = st.sidebar.selectbox("Menu", menu_options)
 
     if choice == "Notas Fiscais":
        notasfiscais_options = ["Selecione uma opção", "Registro 1100"]
        notasfiscais_choice = st.sidebar.selectbox("CAT", notasfiscais_options)
        
        if notasfiscais_choise == "Notas Fiscais":
        st.subheader("Notas Fiscais")
        notas_fiscais()
