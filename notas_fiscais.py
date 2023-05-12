# Importando as bibliotecas necessárias
import streamlit as st
import pandas as pd
from bs4 import BeautifulSoup

# Função para extrair os dados do XML
def extract_data(file):
    # Cria um objeto BeautifulSoup
    bs = BeautifulSoup(file, 'lxml')
    
    # Extrai os dados necessários
    data = {
        'Chave do produto': bs.find('infprot').get('chnfe') if bs.find('infprot') else None,
        'Código de Item': bs.find('det').get('nitem') if bs.find('det') else None,
        'Data de emissão': bs.find('ide').dhemi.string if bs.find('ide') else None,
        'CFOP do produto': bs.find('prod').cfop.string if bs.find('prod') else None,
        'NCM do produto': bs.find('prod').ncm.string if bs.find('prod') else None,
        'Código do produto': bs.find('prod').cprod.string if bs.find('prod') else None,
        'Descrição do Produto': bs.find('prod').xprod.string if bs.find('prod') else None,
        'Quantidade do produto': bs.find('prod').qcom.string if bs.find('prod') else None,
        'EAN do produto': bs.find('prod').cean.string if bs.find('prod') else None,
        'Valor do Produto': bs.find('prod').vprod.string if bs.find('prod') else None,
        'ICMS do produto': bs.find('icms60').vicmssubstituto.string if bs.find('icms60') else None,
        'ICMS ret do produto': bs.find('icms60').vicmsstret.string if bs.find('icms60') else None,
    }
    
    return data
# Cria a interface do Streamlit
st.title('Carregador de Notas Fiscais')

# Cria um seletor de arquivos para vários arquivos
files = st.file_uploader('Upload your XML files', type=['xml'], accept_multiple_files=True)

# Se algum ou mais arquivos foram carregados
if files:
    # Inicializa uma lista vazia para armazenar os dados
    all_data = []

    # Itera sobre os arquivos carregados
    for file in files:
        # Extrai os dados do arquivo XML
        data = extract_data(file)

        # Adiciona os dados à lista
        all_data.append(data)

    # Cria um DataFrame com os dados
    df = pd.DataFrame(all_data)

    # Exibe os dados
    st.write(df)
