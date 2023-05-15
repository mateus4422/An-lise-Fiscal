import streamlit as st
import pandas as pd
import re

def notas_fiscais():
    # Cria a interface do Streamlit
    st.title('Carregador de Notas Fiscais Originais')

    # Cria um seletor de arquivos para vários arquivos
    uploaded_file = st.file_uploader('Upload your XLSX file', type=['xlsx'])

    # Se algum arquivo foi carregado
    if uploaded_file:
        # Lê os dados do arquivo XLSX
        df = pd.read_excel(uploaded_file)

        # Remove caracteres especiais das colunas 'Código de Produto' (cProd), 'CFOP' e 'NCM'
        if 'Código de Produto' in df.columns:
            df['Código de Produto'] = df['Código de Produto'].apply(lambda x: re.sub(r'\W+', '', str(x)))

        if 'CFOP' in df.columns:
            df['CFOP'] = df['CFOP'].apply(lambda x: re.sub(r'\W+', '', str(x)))

        if 'NCM' in df.columns:
            df['NCM'] = df['NCM'].apply(lambda x: re.sub(r'\W+', '', str(x)))

        # Exibe o dataframe com as alterações
        st.write(df)

        # Solicita ao usuário para inserir a chave e o código do produto
        chave = st.text_input("Digite a Chave Original (chNFe)")
        codigo_produto = st.text_input("Digite o Código do Produto (Código de Produto)")

        # Se o usuário digitou a chave e o código do produto
        if chave and codigo_produto:
            # Filtra o dataframe para mostrar apenas as linhas que correspondem à chave e ao código do produto
            filtered_df = df[(df['chNFe'] == chave) & (df['Código de Produto'] == codigo_produto)]
            
            # Exibe os dados filtrados
            st.write(filtered_df)

notas_fiscais()
