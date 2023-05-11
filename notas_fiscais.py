import streamlit as st
import pandas as pd
import xml.etree.ElementTree as ET

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
                # Carregar o XML
                tree = ET.parse(xml_file)
                root = tree.getroot()

                for nfe in root.findall(".//NFe/infNFe"):
                    chave = nfe.find(".//ide/Id").text
                    item = nfe.find(".//det/item").text
                    data_emissao = nfe.find(".//ide/dhEmi").text
                    cfop = nfe.find(".//det/imposto/ICMS/ICMS00/CFOP").text
                    ncm = nfe.find(".//det/prod/NCM").text
                    codigo_produto = nfe.find(".//det/prod/cProd").text
                    descricao = nfe.find(".//det/prod/xProd").text
                    quantidade = nfe.find(".//det/prod/qCom").text
                    cean = nfe.find(".//det/prod/cEAN").text
                    vprod = nfe.find(".//det/prod/vProd").text
                    icms_vbcst = nfe.find(".//det/imposto/ICMS/ICMS10/vBCST").text
                    icms_vbcstret = nfe.find(".//det/imposto/ICMS/ICMS10/vBCSTRet").text

                    df = df.append({"Chave da Nota": chave, "Item da Nota": item, "Data de Emissão": data_emissao,
                                    "CFOP": cfop, "NCM": ncm, "Código do Produto": codigo_produto,
                                    "Descrição da Nota": descricao, "Quantidade": quantidade,
                                    "cEAN": cean, "vProd": vprod, "ICMS vBCST": icms_vbcst,
                                    "ICMS vBCSTRet": icms_vbcstret}, ignore_index=True)

                st.dataframe(df)

            except Exception as e:
                st.error(f"Erro ao processar o arquivo XML: {e}")

if __name__ == "__main__":
    notas_fiscais()
