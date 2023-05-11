import streamlit as st
from notas_fiscais import notas_fiscais
from notas_complementares import notas_complementares
from efd import efd
from cat import cat
from conversao_codigo import conversao_codigo
from analise_fiscal import analise_fiscal

def main():
    st.title("Aplicativo de Análise Fiscal")

    menu_options = ["Notas Fiscais", "Notas Complementares", "EFD", "CAT", "Conversão de Código (NF Original)", "Análise Fiscal"]
    choice = st.sidebar.selectbox("Menu", menu_options)

    if choice == "Notas Fiscais":
        notas_fiscais()
    elif choice == "Notas Complementares":
        notas_complementares()
    elif choice == "EFD":
        efd()
    elif choice == "CAT":
        cat()
    elif choice == "Conversão de Código (NF Original)":
        conversao_codigo()
    elif choice == "Análise Fiscal":
        analise_fiscal()

if __name__ == "__main__":
    main()
