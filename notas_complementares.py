import streamlit as st
import pandas as pd

def notas_complementares():
    # Cria a interface do Streamlit
    st.title('Análise de Notas Fiscais')

    # Cria um seletor de arquivos
    file = st.file_uploader('Upload your Excel file', type=['xlsx'])

    # Se um arquivo foi carregado
    if file:
        df = pd.read_excel(file)


        st.write(df)  # Exibir o DataFrame

        # Solicitar ao usuário a chave e o código do produto
        chave = st.text_input('Digite a Chave Original')
        codigo_produto = st.text_input('Digite o Código de Produto')

        if chave and codigo_produto:
            # Filtrar o DataFrame com base na chave e no código do produto
            filtered_df = df[(df['Chave Complementar'] == chave) & (df['Código de Produto'] == codigo_produto)]
            
            st.write(filtered_df)  # Exibir o DataFrame filtrado

notas_complementares()
