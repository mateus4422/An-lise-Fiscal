import streamlit as st
import pandas as pd

def notas_complementares():
    # Cria a interface do Streamlit
    st.title('Carregador de Notas Fiscais')

    # Cria um seletor de arquivos
    file = st.file_uploader('Upload your Excel file', type=['xlsx'])

    # Se um arquivo foi carregado
    if file:
        # Carrega os dados do arquivo Excel
        df = pd.read_excel(file)

        # Solicita ao usuário para inserir a chave e o código do produto
        chave = st.text_input('Enter the key')
        codigo_produto = st.text_input('Enter the product code')

        # Filtra o DataFrame com base na chave e no código do produto
        filtered_df = df[(df['Chave Complementar'] == chave) & (df['Código do produto'] == codigo_produto)]

        # Exibe os dados filtrados
        st.write(filtered_df)

st.write()
