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

        # Exibe o dataframe completo
        st.write(df)

        # Obtem a lista de colunas do dataframe
        colunas = df.columns

        # Cria um dicionário para mapear os tipos de dados para os widgets do Streamlit
        tipos_dados = {
            'int64': 'Inteiro',
            'float64': 'Decimal',
            'datetime64[ns]': 'Data'
        }

        # Cria filtros para cada coluna do dataframe
        for coluna in colunas:
            # Obtém o tipo de dado da coluna
            tipo_dado = df[coluna].dtype

            # Obtém a descrição do tipo de dado para exibir no seletor
            tipo_dado_descricao = tipos_dados.get(str(tipo_dado), 'Texto')

            # Exibe o seletor de formato para a coluna atual
            formato_texto = st.selectbox(f'Selecione o formato para a coluna {coluna}', options=['Texto', 'Inteiro', 'Decimal', 'Data'])

            # Converte o formato selecionado para o tipo correspondente
            if formato_texto == 'Inteiro':
                df[coluna] = df[coluna].astype(int)
            elif formato_texto == 'Decimal':
                df[coluna] = df[coluna].astype(float)
            elif formato_texto == 'Data':
                df[coluna] = pd.to_datetime(df[coluna], errors='coerce')

        # Exibe o dataframe atualizado com os formatos selecionados
        st.write(df)

        # Solicita ao usuário para inserir a chave e o código do produto
        chave = st.text_input("Digite a Chave Complementar (chNFe)")
        codigo_produto = st.text_input("Digite o Código do Produto (cProd)")

        # Se o usuário digitou a chave e o código do produto
        if chave and codigo_produto:
            # Filtra o dataframe para mostrar apenas as linhas que correspondem à chave e ao código do produto
            filtered_df = df[(df['chNFe'] == chave) & (df['cProd'] == codigo_produto)]
            
            # Exibe os dados filtrados
            st.write(filtered_df)

notas_complementares()
