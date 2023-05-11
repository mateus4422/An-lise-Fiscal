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

                for nfe in root.findall(".//{http://www.portalfiscal.inf.br/nfe}NFe"):
                    chave = nfe.find(".//{http://www.portalfiscal.inf.br/nfe}infNFe/{http://www.portalfiscal.inf.br/nfe}ide/{http://www.portalfiscal.inf.br/nfe}Id").text

                    for det in nfe.findall(".//{http://www.portalfiscal.inf.br/nfe}infNFe/{http://www.portalfiscal.inf.br/nfe}det"):
                        item = det.find("{http://www.portalfiscal.inf.br/nfe}prod/{http://www.portalfiscal.inf.br/nfe}cProd").text
                        data_emissao = det.find("{http://www.portalfiscal.inf.br/nfe}infNFe/{http://www.portalfiscal.inf.br/nfe}ide/{http://www.portalfiscal.inf.br/nfe}dhEmi").text
                        cfop = det.find("{http://www.portalfiscal.inf.br/nfe}prod/{http://www.portalfiscal.inf.br/nfe}CFOP").text
                        ncm = det.find("{http://www.portalfiscal.inf.br/nfe}prod/{http://www.portalfiscal.inf.br/nfe}NCM").text
                        codigo_produto = det.find("{http://www.portalfiscal.inf.br/nfe}prod/{http://www.portalfiscal.inf.br/nfe}cProd").text
                        descricao = det.find("{http://www.portalfiscal.inf.br/nfe}prod/{http://www.portalfiscal.inf.br/nfe}xProd").text
                        quantidade = det.find("{http://www.portalfiscal.inf.br/nfe}prod/{http://www.portalfiscal.inf.br/nfe}qCom").text
                        cean = det.find("{http://www.portalfiscal.inf.br/nfe}prod/{http://www.portalfiscal.inf.br/nfe}cEAN").text
                        vprod = det.find("{http://www.portalfiscal.inf.br/nfe}prod/{http://www.portalfiscal.inf.br/nfe}vProd").text
                        icms_vbcst = det.find("{http://www.portalfiscal.inf.br/nfe}imposto/{http://www.portalfiscal.inf.br/nfe}ICMS/{http://www.portalfiscal.inf.br/nfe}ICMS10/{http://www.portalfiscal.inf.br/nfe}vBCST").text
                        icms_vbcstret = det.find("{http://www.portalfiscal.inf.br/nfe}imposto/{http://www.portalfiscal.inf.br/nfe}ICMS/{http://www.portalfiscal.inf.br/nfe}ICMS10/{http://www.portalfiscal.inf.br/nfe}vBCSTRet").text

                        # Adicionar os dados ao DataFrame
                        df = df.append({"Chave da Nota": chave,
                                        "Item da Nota": item,
                                        "Data de Emissão": data_emissao,
                                        "CFOP": cfop,
                                        "NCM": ncm,
                                        "Código do Produto": codigo_produto,
                                        "Descrição da Nota": descricao,
                                        "Quantidade": quantidade,
                                        "cEAN": cean,
                                        "vProd": vprod,
                                        "ICMS vBCST": icms_vbcst,
                                        "ICMS vBCSTRet": icms_vbcstret}, ignore_index=True)
            except Exception as e:
                st.error(f"Erro ao processar o arquivo XML: {e}")

        # Exibir o DataFrame
        st.write("Dados das Notas Fiscais:")
        st.dataframe(df)

if __name__ == "__main__":
    notas_fiscais()
