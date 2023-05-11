import streamlit as st
from notas_fiscais import notas_fiscais
'from notas_complementares import notas_complementares
'from efd import efd
'from cat import cat'
'from conversao_codigo import conversao_codigo
'from analise_fiscal import analise_fiscal'

def main():
    st.title("Aplicativo de Análise Fiscal")

    menu_options = ["Notas Fiscais", "Notas Complementares", "EFD", "CAT", "Conversão de Código (NF Original)", "Análise Fiscal"]
    choices = st.sidebar.multiselect("Menu", menu_options)

    if "Notas Fiscais" in choices:
        st.write("## Notas Fiscais")
        notas_fiscais()

    if "Notas Complementares" in choices:
        st.write("## Notas Complementares")
        notas_complementares()

    if "EFD" in choices:
        st.write("## EFD")
        efd()

    if "CAT" in choices:
        st.write("## CAT")
        cat()

    if "Conversão de Código (NF Original)" in choices:
        st.write("## Conversão de Código (NF Original)")
        conversao_codigo()

    if "Análise Fiscal" in choices:
        st.write("## Análise Fiscal")
        analise_fiscal()

if __name__ == "__main__":
    main()
