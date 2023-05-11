import streamlit as st
from notas_fiscais import notas_fiscais

def main():
    st.title("Aplicativo de Análise Fiscal")

    st.sidebar.markdown("Notas Fiscais")
    st.sidebar.markdown("Selecione a opção:")
    
    notas_fiscais()

if __name__ == "__main__":
    main()
