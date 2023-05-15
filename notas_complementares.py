import streamlit as st
import pandas as pd

def notas_complementares():
    # Cria a interface do Streamlit
    st.title('Carregador de Notas Fiscais Complementares')

    # Cria um seletor de arquivos para vários arquivos
    uploaded_file = st.file_uploader('Upload your XLSX file', type=['xlsx'])

    # Se algum arquivo foi carregado
    if uploaded_file:
        # Lê os dados do arquivo XLSX
        df = pd.read_excel(uploaded_file)

        # Substitui as vírgulas por nada (remove as vírgulas) na coluna 'cProd'
        df['cProd'] = df['cProd'].str.replace(',', '')

        # Substitui as vírgulas por nada (remove as vírgulas) na coluna 'CFOP'
        df['CFOP'] = df['CFOP'].str.replace(',', '')

        # Substitui as vírgulas por pontos na coluna 'NCM'
        df['NCM'] = df['NCM'].str.replace(',', '.')

        # Exibe o dataframe completo
        st.write(df)

        # Solicita ao usuário para inserir a chave e o código do produto
        chave = st.text_input("Digite a Chave Original (chNFe)")
        codigo_produto = st.text_input("Digite o Código do Produto (cProd)")

        # Se o usuário digitou a chave e o código do produto
        if chave and codigo_produto:
            # Filtra o dataframe para mostrar apenas as linhas que correspondem à chave e ao código do produto
            filtered_df = df[(df['chNFe'] == chave) & (df['cProd'] == codigo_produto)]
            
            # Exibe os dados filtrados
            st.write(filtered_df)

notas_complementares()
