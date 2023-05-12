import streamlit as st
import pandas as pd
from bs4 import BeautifulSoup

def notas_fiscais():
    # Função para extrair os dados do XML
    def extract_data(file):
        bs = BeautifulSoup(file, 'xml')

        chave_nfe = bs.find('infProt').get('chNFe') if bs.find('infProt') else None

        data = []
        for det in bs.find_all('det'):
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
            data.append(product_data)

        return data
    # Função principal
    def main():
        st.title('Carregador de Notas Fiscais')

        files = st.file_uploader('Upload your XML files', type=['xml'], accept_multiple_files=True)

        if files:
            all_data = []
            for file in files:
                file_data = extract_data(file)
                all_data.extend(file_data)

            df = pd.DataFrame(all_data)
            st.write(df)

    # Execução principal
    if __name__ == '__main__':
        main()
