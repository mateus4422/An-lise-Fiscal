# Importando as bibliotecas necessárias
import streamlit as st
import pandas as pd
from bs4 import BeautifulSoup

def notas_fiscais():
    # Função para extrair os dados do XML
    def extract_data(file):
        # Cria um objeto BeautifulSoup com o parser XML
        bs = BeautifulSoup(file, 'xml')

        # Extrai a chave de acesso da nota fiscal
        chave_nfe = bs.find('infProt').get('chNFe') if bs.find('infProt') else None

        # Inicializa uma lista vazia para armazenar os dados de todos os produtos
        data = []

        # Itera sobre todos os elementos <det>
        for det in bs.find_all('det'):
            # Extrai os dados necessários
            product_data = {
                'Chave do produto': chave_nfe,
                'Código de Item': det.get('nItem'),
                'Data de emissão': bs.find('ide').find('dhEmi').string if bs.find('ide') and bs.find('ide').find('dhEmi') else None,
                'CFOP do produto': det.find('prod').find('CFOP').string if det.find('prod') and det.find('prod').find('CFOP') else None,
                'NCM do produto': det.find('prod').find('NCM').string if det.find('prod') and det.find('prod').find('NCM') else None,
                'Código do produto': det.find('prod').find('cProd').string if det.find('prod') and det.find('prod').find('cProd') else None,
                'Descrição do Produto': det.find('prod').find('xProd').string if det.find('prod') and det.find('prod').find('xProd') else None,
                'Quantidade do produto': det.find('prod').find('qCom').string if det.find('prod') and det.find('prod').find('qCom') else None,
                'EAN do produto': det.find('prod').find('cEAN').string if det.find('prod') and det.find('prod').find('cEAN') else None,
                'Valor do Produto': det.find('prod').find('vProd').string if det.find('prod') and det.find('prod').find('vProd') else None,
                'ICMS do produto': det.find('ICMS60').find('vICMSSubstituto').string if det.find('ICMS60') and det.find('ICMS60').find('vICMSSubstituto') else None,
                'ICMS ret do produto': det.find('ICMS60').find('vICMSSTRet').string if det.find('ICMS60') and det.find('ICMS60').find('vICMSSTRet') else None,
            }

            # Adiciona os dados do produto à lista
            data.append(product_data)

        return data
    # Cria a interface do Streamlit
    # Cria a interface do Streamlit
    st.title('Carregador de Notas Fiscais')

    # Cria um seletor de arquivos para vários arquivos
    files = st.file_uploader('Upload your XML files', type=['xml'], accept_multiple_files=True)

    # Se algum ou mais arquivos foram carregados
    if files:
        # Inicializa uma lista vazia para armazenar os DataFrames individuais de cada arquivo
        dataframes = []

        # Itera sobre os arquivos carregados
        for file in files:
            # Extrai os dados do arquivo XML
            file_data = extract_data(file)

            # Cria um DataFrame com os dados do arquivo
            file_df = pd.DataFrame(file_data)

            # Adiciona o DataFrame do arquivo à lista
            dataframes.append(file_df)

        # Concatena todos os DataFrames em um DataFrame geral
        data = pd.concat(dataframes, ignore_index=True)

        # Exibe os dados
        st.write(data)


