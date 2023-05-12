# Importando as bibliotecas necessárias
import streamlit as st
import pandas as pd
from bs4 import BeautifulSoup

def notas_fiscais()
    # Função para extrair os dados do XML
    def extract_data(file):
        # Cria um objeto BeautifulSoup usando o parser XML (lxml)
        bs = BeautifulSoup(file, 'xml')

        # Extrai os dados necessários
        data = {
            'Chave do produto': bs.find('infProt').get('chNFe') if bs.find('infProt') else None,
            'Código de Item': bs.find('det').get('nItem') if bs.find('det') else None,
            'Data de emissão': bs.find('ide').dhEmi.string if bs.find('ide') else None,
            'CFOP do produto': bs.find('prod').CFOP.string if bs.find('prod') else None,
            'NCM do produto': bs.find('prod').NCM.string if bs.find('prod') else None,
            'Código do produto': bs.find('prod').cProd.string if bs.find('prod') else None,
            'Descrição do Produto': bs.find('prod').xProd.string if bs.find('prod') else None,
            'Quantidade do produto': bs.find('prod').qCom.string if bs.find('prod') else None,
            'EAN do produto': bs.find('prod').cEAN.string if bs.find('prod') else None,
            'Valor do Produto': bs.find('prod').vProd.string if bs.find('prod') else None,
            'ICMS do produto': bs.find('ICMS60').vICMSSubstituto.string if bs.find('ICMS60') else None,
            'ICMS ret do produto': bs.find('ICMS60').vICMSSTRet.string if bs.find('ICMS60') else None,
        }

        # Retorna os dados como um DataFrame
        return pd.DataFrame([data])

    # Cria a interface do Streamlit
    st.title('Carregador de Notas Fiscais')

    # Cria um seletor de arquivos para vários arquivos
    files = st.file_uploader('Upload your XML files', type=['xml'], accept_multiple_files=True)

    # Se algum ou mais arquivos foram carregados
    if files:
        # Inicializa um DataFrame vazio
        data = pd.DataFrame()

        # Loop por todos os arquivos e extrai os dados
        for file in files:
            file_data = extract_data(file)
            data = data.append(file_data, ignore_index=True)

        # Exibe os dados
        st.write(data)
