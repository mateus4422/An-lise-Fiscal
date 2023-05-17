import streamlit as st
import pandas as pd

def item_complementar():
    def read_xlsx(file):
        df = pd.read_excel(file)

        # Remova quaisquer caracteres não numéricos e converta para int
        df['cprod'] = df['cprod'].str.replace(',', '').str.extract('(\d+)', expand=False).astype(int)

        return df

    st.title("Leitor de Arquivos Excel")

    uploaded_file = st.file_uploader("Selecione o arquivo Excel:", type=["xlsx"], key="item_complementar")


    if uploaded_file is not None:
        df = read_xlsx(uploaded_file)
        
        # Renomeie as colunas
        df.rename(columns={df.columns[0]: 'Chave', df.columns[1]: 'Chave + Código + Ítem'}, inplace=True)

        st.write(df)

