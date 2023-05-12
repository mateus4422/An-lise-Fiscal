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
            'Chave do produto': bs.find('infprot').get('chnfe'),
            'Código de Item': bs.find('det').get('nitem'),
            'Data de emissão': bs.find('ide').dhemi.string,
            'CFOP do produto': bs.find('prod').cfop.string,
            'NCM do produto': bs.find('prod').ncm.string,
            'Código do produto': bs.find('prod').cprod.string,
            'Descrição do Produto': bs.find('prod').xprod.string,
            'Quantidade do produto': bs.find('prod').qcom.string,
            'EAN do produto': bs.find('prod').cean.string,
            'Valor do Produto': bs.find('prod').vprod.string,
            'ICMS do produto': bs.find('icms60').vicmssubstituto.string,
            'ICMS ret do produto': bs.find('icms60').vicmsstret.string,
        }

        # Retorna os dados como um DataFrame
        return pd.DataFrame([data])

    # Cria a interface do Streamlit
    st.title('Carregador de Notas Fiscais')

    # Cria um seletor de arquivos
    file = st.file_uploader('Upload your XML file', type=['xml'])

    # Se um arquivo foi carregado
    if file is not None:
        # Extrai os dados do arquivo
        data = extract_data(file)

        # Exibe os dados
        st.write(data)
