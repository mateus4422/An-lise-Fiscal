import streamlit as st
import pandas as pd
import xmltodict

def notas_fiscais():
    st.header("Notas Fiscais")

    # Selecionar múltiplos arquivos XML
    xml_files = st.file_uploader("Selecione os arquivos XML das notas fiscais", accept_multiple_files=True, type=".xml")

    if xml_files:
        df = pd.DataFrame(columns=["Chave da Nota", "Item da Nota", "Data de Emissão", "CFOP", "NCM", "Código do Produto",
                                   "Descrição da Nota", "Quantidade", "cEAN", "vProd", "ICMS vBCST", "ICMS vBCSTRet"])

        for xml_file in xml_files:
            st.subheader(f"Arquivo: {xml_file.name}")

            try:
                # Carregar o XML e converter para dicionário
                xml_dict = xmltodict.parse(xml_file.read())

                # Extrair os dados dos campos desejados
                chave = xml_dict['NFe']['infNFe']['ide']['Id']
                for item in xml_dict['NFe']['infNFe']['det']:
                    item_nota = item['nItem']
                    data_emissao = xml_dict['NFe']['infNFe']['ide']['dhEmi']
                    cfop = item['imposto']['ICMS']['ICMS00']['CFOP']
                    ncm = item['prod']['NCM']
                    codigo_produto = item['prod']['cProd']
                    descricao = item['prod']['xProd']
                    quantidade = item['prod']['qCom']
                    cean = item['prod']['cEAN']
                    vprod = item['prod']['vProd']
                    icms_vbcst = item['imposto']['ICMS']['ICMS10']['vBCST']
                    icms_vbcstret = item['imposto']['ICMS']['ICMS10']['vBCSTRet']

                    df = df.append({"Chave da Nota": chave, "Item da Nota": item_nota, "Data de Emissão": data_emissao,
                                    "CFOP": cfop, "NCM": ncm, "Código do Produto": codigo_produto,
                                    "Descrição da Nota": descricao, "Quantidade": quantidade,
                                    "cEAN": cean, "vProd": vprod, "ICMS vBCST": icms_vbcst,
                                    "ICMS vBCSTRet": icms_vbcstret}, ignore_index=True)

                st.dataframe(df)

            except Exception as e:
                st.error(f"Erro ao processar o arquivo XML: {e}")

if __name__ == "__main__":
    notas_fiscais()
