import streamlit as st
import pandas as pd
from bs4 import BeautifulSoup

def notas_complementares():
    # Função para extrair os dados do XML
    def extract_data(file):
        bs = BeautifulSoup(file, 'xml')

        chave_nfe = bs.find('chNFe').text if bs.find('chNFe') else None
        chave_original = bs.find('NFref').find('refNFe').text if bs.find('NFref') and bs.find('NFref').find('refNFe') else None

        data = []
        for det in bs.find_all('det'):
            product_data = {
                'Chave Complementar': chave_nfe,
                'Chave Original': chave_original,
                'Código de Item': det.get('nItem'),
                'Código do produto': det.find('prod').find('cProd').string if det.find('prod') and det.find('prod').find('cProd') else None,
                'EAN do produto': det.find('prod').find('cEAN').string if det.find('prod') and det.find('prod').find('cEAN') else None,
                'Descrição do Produto': det.find('prod').find('xProd').string if det.find('prod') and det.find('prod').find('xProd') else None,
                'NCM do produto': det.find('prod').find('NCM').string if det.find('prod') and det.find('prod').find('NCM') else None,
                'CFOP do produto': det.find('prod').find('CFOP').string if det.find('prod') and det.find('prod').find('CFOP') else None,
                'Quantidade do produto': det.find('prod').find('qCom').string if det.find('prod') and det.find('prod').find('qCom') else None,
                'Valor do Produto': det.find('prod').find('vProd').string if det.find('prod') and det.find('prod').find('vProd') else None,
                'ICMS Complementar': det.find('ICMS60').find('vICMSSTRet').string if det.find('ICMS60') and det.find('ICMS60').find('vICMSSTRet') else None,
            }
            data.append(product_data)

        return data

    # Cria a interface do Streamlit
    st.title('Carregador de Notas Complementares')

    # Cria um seletor de arquivos para vários arquivos
    files = st.file_uploader('Upload your XML files', type=['xml'], accept_multiple_files=True)

    # Se algum ou mais arquivos foram carregados
    if files:
        # Inicializa uma lista vazia para armazenar todos os dados
        all_data = []

        # Itera sobre os arquivos carregados
        for file in files:
            # Extrai os dados do arquivo XML
            file_data = extract_data(file)

            # Adiciona os dados do arquivo à lista geral
            all_data.extend(file_data)

        # Cria um DataFrame com todos os dados
        df = pd.DataFrame(all_data)

        # Exibe os dados
        st.write(df)
