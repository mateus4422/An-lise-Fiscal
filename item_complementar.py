import streamlit as st
import pandas as pd

def item_complementar():
    def read_xlsx(file):
        df = pd.read_excel(file)

        # Renomeie a coluna 2
        df.rename(columns={df.columns[2]: 'Código do Produto'}, inplace=True)
        
        # Remova quaisquer caracteres não numéricos e converta para int
        df['Código do Produto'] = df['Código do Produto'].str.replace(',', '').str.extract('(\d+)', expand=False).astype(int)

        return df

    st.title("Leitor de Arquivos Excel")

    uploaded_file = st.file_uploader("Selecione o arquivo Excel:", type=["xlsx"], key="item_complementar")

    if uploaded_file is not None:
        df = read_xlsx(uploaded_file)

        st.write(df)
