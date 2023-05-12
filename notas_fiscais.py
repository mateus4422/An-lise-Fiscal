# Importando as bibliotecas necessárias
import streamlit as st
import pandas as pd
from bs4 import BeautifulSoup

def notas_fiscais():
    # Função para extrair os dados do XML
    def extract_data(file):
        # Cria um objeto BeautifulSoup
        bs = BeautifulSoup(file, 'lxml')

        # Extrai os dados necessários
        data = {
            'Chave do produto': bs.find('infProt').get('chNFe'),
            'Código de Item': bs.find('det').get('nItem'),
            'Data de emissão': bs.find('ide').dhEmi.string,
            'CFOP do produto': bs.find('prod').CFOP.string,
            'NCM do produto': bs.find('prod').NCM.string,
            'Código do produto': bs.find('prod').cProd.string,
            'Descrição do Produto': bs.find('prod').xProd.string,
            'Quantidade do produto': bs.find('prod').qCom.string,
            'EAN do produto': bs.find('prod').cEAN.string,
            'Valor do Produto': bs.find('prod').vProd.string,
            'ICMS do produto': bs.find('ICMS60').vICMSSubstituto.string,
            'ICMS ret do produto': bs.find('ICMS60').vICMSSTRet.string,
        }

        # Retorna os dados como um DataFrame
        return pd.DataFrame([data])
    # Cria a interface do Streamlit
    st.title('Carregador de Notas Fiscais')

    # Cria um seletor de arquivos para vários arquivos
    files = st.file_uploader('Upload your XML files', type=['xml'], accept_multiple_files=True)

    # Se um ou mais arquivos foram carregados
    if files:
        # Inicializa um DataFrame vazio
        data = pd.DataFrame()

        # Loop por todos os arquivos e extrai os dados
        for file in files:
            file_data = extract_data(file)
            data = data.append(file_data, ignore_index=True)

        # Exibe os dados
        st.write(data)
