import streamlit as st
from notas_fiscais import notas_fiscais
from notas_complementares import notas_complementares
from efd import efd
from cat import cat
from ítem_complementar import item_complementar
#from analise_fiscal import analise_fiscal

def main():
    st.title("Aplicativo de Análise Fiscal")

    st.sidebar.title("Menu")
    menu_options = ["Notas Fiscais", "Notas Complementares", "EFD", "CAT", "Conversão de Código (NF Original)","Ítem Complementar","Análise Fiscal"]
    choice = st.sidebar.radio("Selecione uma opção", menu_options)

    if choice == "Notas Fiscais":
        notas_fiscais()

    if choice == "Notas Complementares":
        notas_complementares()

    if choice == "EFD":
        efd()

    if choice == "CAT":
        cat()

    if choice == "Conversão de Código (NF Original)":
        conversao_codigo()

    if choice == "Conversão de Ítem (NF Complementar)":
        item_complementar()
        
    if choice == "Análise Fiscal":
        analise_fiscal()

if __name__ == "__main__":
    main()
