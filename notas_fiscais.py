# Importando as bibliotecas necessárias
import streamlit as st
import pandas as pd
from bs4 import BeautifulSoup

def notas_fiscais():

    # Função para extrair os dados do XML
    def extract_data(file):
        # Cria um objeto BeautifulSoup
        bs = BeautifulSoup(file, 'lxml')

        # Inicializa uma lista vazia para armazenar os dados de todos os produtos
        data = []

        # Extrai a chave de acesso da nota fiscal
        chave_nfe = bs.find('infProt').get('chNFe') if bs.find('infProt') else None

        # Itera sobre todos os elementos <det>
        for det in bs.find_all('det'):
            # Extrai os dados necessários
            product_data = {
                'Chave do produto': chave_nfe,
                'Código de Item': det.get('nItem'),
                'Data de emissão': bs.find('ide').dhEmi.string,
                'CFOP do produto': det.find('prod').CFOP.string,
                'NCM do produto': det.find('prod').NCM.string,
                'Código do produto': det.find('prod').cProd.string,
                'Descrição do Produto': det.find('prod').xProd.string,
                'Quantidade do produto': det.find('prod').qCom.string,
                'EAN do produto': det.find('prod').cEAN.string,
                'Valor do Produto': det.find('prod').vProd.string,
                'ICMS do produto': det.find('ICMS60').vICMSSubstituto.string if det.find('ICMS60') else None,
                'ICMS ret do produto': det.find('ICMS60').vICMSSTRet.string if det.find('ICMS60') else None,
            }

            # Adiciona os dados do produto à lista
            data.append(product_data)

        return data
    # Cria a interface do Streamlit
    st.title('Carregador de Notas Fiscais')

    # Cria um seletor de arquivos para vários arquivos
    files = st.file_uploader('Upload your XML files', type=['xml'], accept_multiple_files=True)

    # Se algum ou mais arquivos foram carregados
    if files:
        # Inicializa um DataFrame vazio
        data = pd.DataFrame()

        # Itera sobre os arquivos carregados
        for file in files:
            # Extrai os dados do arquivo XML
            file_data = extract_data(file)

            # Cria um DataFrame com os dados do arquivo
            file_df = pd.DataFrame(file_data)

            # Adiciona os dados do arquivo ao DataFrame geral
            data = data.append(file_df, ignore_index=True)

        # Exibe os dados
        st.write(data)
