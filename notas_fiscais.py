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
        chave_nfe = bs.find('infprot').chnfe.string if bs.find('infprot') and bs.find('infprot').chnfe else None

        # Itera sobre todos os elementos <det>
        for det in bs.find_all('det'):
            # Extrai os dados necessários
            product_data = {
                'Chave do produto': chave_nfe,
                'Código de Item': det.get('nitem'),
                'Data de emissão': bs.find('ide').dhemi.string,
                'CFOP do produto': det.prod.cfop.string,
                'NCM do produto': det.prod.ncm.string,
                'Código do produto': det.prod.cprod.string,
                'Descrição do Produto': det.prod.xprod.string,
                'Quantidade do produto': det.prod.qcom.string,
                'EAN do produto': det.prod.cean.string,
                'Valor do Produto': det.prod.vprod.string,
                'ICMS do produto': det.find('icms60').vicmssubstituto.string if det.find('icms60') else None,
                'ICMS ret do produto': det.find('icms60').vicmsstret.string if det.find('icms60') else None,
            }

            # Adiciona os dados do produto à lista
            data.append(product_data)

        # Retorna os dados como um DataFrame
        return pd.DataFrame(data)

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

    # Cria filtros para Chave do produto, EAN e Código do produto
    chave_filter = st.multiselect('Chave do produto', options=data['Chave do produto'].unique())
    ean_filter = st.multiselect('EAN do produto', options=data['EAN do produto'].unique())
    codigo_filter = st.multiselect('Código do produto', options=data['Código do produto'].unique())

    # Aplica os filtros
    if chave_filter:
        data = data[data['Chave do produto'].isin(chave_filter)]
    if ean_filter:
        data = data[data['EAN do produto'].isin(ean_filter)]
    if codigo_filter:
        data = data[data['Código do produto'].isin(codigo_filter)]

    # Exibe os dados
    st.write(data)
