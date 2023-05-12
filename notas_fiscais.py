# Importando as bibliotecas necessárias
import streamlit as st
import pandas as pd
from bs4 import BeautifulSoup

# Função para extrair os dados do XML
def notas_fiscais(file):
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

# Cria um seletor de arquivos para vários arquivos
files = st.file_uploader('Upload your XML files', type=['xml'], accept_multiple_files=True)

# Se um ou mais arquivos foram carregados
if files:
    # Inicializa uma lista para armazenar os DataFrames
    dataframes = []

    # Loop por todos os arquivos e extrai os dados
    for file in files:
        file_data = notas_fiscais(file)
        dataframes.append(file_data)

    # Concatena todos os dataframes
    data = pd.concat(dataframes, ignore_index=True)

    # Exibe os dados
    st.write(data)
