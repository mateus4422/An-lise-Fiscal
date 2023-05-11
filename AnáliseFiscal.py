import streamlit as st
from notas_fiscais import notas_fiscais
#from notas_complementares import notas_complementares
#from efd import efd
#from cat import cat'
#from conversao_codigo import conversao_codigo'
#from analise_fiscal import analise_fiscal

def main():
    st.title("Aplicativo de Análise Fiscal")

    menu_options = ["Notas Fiscais", "Notas Complementares", "EFD", "CAT", "Conversão de Código (NF Original)", "Análise Fiscal"]
    choices = st.sidebar.multiselect("Menu", menu_options)

    for choice in choices:
        if choice == "Notas Fiscais":
            st.write("## Notas Fiscais")
            notas_fiscais()

        if choice == "Notas Complementares":
            st.write("## Notas Complementares")
            notas_complementares()

        if choice == "EFD":
            st.write("## EFD")
            efd()

        if choice == "CAT":
            st.write("## CAT")
            cat()

        if choice == "Conversão de Código (NF Original)":
            st.write("## Conversão de Código (NF Original)")
            conversao_codigo()

        if choice == "Análise Fiscal":
            st.write("## Análise Fiscal")
            analise_fiscal()

if __name__ == "__main__":
    main()
