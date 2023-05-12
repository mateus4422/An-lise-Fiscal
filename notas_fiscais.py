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
        infprot = bs.find('infprot')
        chave_nfe = infprot.chnfe.string if infprot and infprot.chnfe else None

        # Itera sobre todos os elementos <det>
        for det in bs.find_all('det'):
            # Extrai os dados necessários
            prod = det.find('prod')
            icms60 = det.find('icms60')

            product_data = {
                'Chave do produto': chave_nfe,
                'Código de Item': det.get('nitem'),
                'Data de emissão': bs.find('ide').dhemi.string if bs.find('ide') and bs.find('ide').dhemi else None,
                'CFOP do produto': prod.cfop.string if prod and prod.cfop else None,
                'NCM do produto': prod.ncm.string if prod and prod.ncm else None,
                'Código do produto': prod.cprod.string if prod and prod.cprod else None,
                'Descrição do Produto': prod.xprod.string if prod and prod.xprod else None,
                'Quantidade do produto': prod.qcom.string if prod and prod.qcom else None,
                'EAN do produto': prod.cean.string if prod and prod.cean else None,
                'Valor do Produto': prod.vprod.string if prod and prod.vprod else None,
                'ICMS do produto': icms60.vicmssubstituto.string if icms60 and icms60.vicmssubstituto else None,
                'ICMS ret do produto': icms60.vicmsstret.string if icms60 and icms60.vicmsstret else None,
            }

            # Adiciona os dados do produto à lista
            data.append(product_data)

        # Retorna os dados como um DataFrame
        return pd.DataFrame(data)
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
