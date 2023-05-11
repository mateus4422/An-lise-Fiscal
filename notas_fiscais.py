import streamlit as st
import xml.etree.ElementTree as ET

def notas_fiscais():
    st.header("Notas Fiscais")

    # Selecionar múltiplos arquivos XML
    xml_files = st.file_uploader("Selecione os arquivos XML das notas fiscais", accept_multiple_files=True, type=".xml")

    if xml_files:
        for xml_file in xml_files:
            st.subheader(f"Arquivo: {xml_file.name}")

            try:
                # Carregar o XML
                tree = ET.parse(xml_file)
                root = tree.getroot()

                for nfe in root.findall(".//NFe"):
                    chave = nfe.find(".//chave").text
                    item = nfe.find(".//item").text
                    data_emissao = nfe.find(".//data_emissao").text
                    cfop = nfe.find(".//cfop").text
                    ncm = nfe.find(".//ncm").text
                    codigo_produto = nfe.find(".//codigo_produto").text
                    descricao = nfe.find(".//descricao").text
                    quantidade = nfe.find(".//quantidade").text
                    cean = nfe.find(".//cean").text
                    vprod = nfe.find(".//vprod").text
                    icms_vbcst = nfe.find(".//icms_vbcst").text
                    icms_vbcstret = nfe.find(".//icms_vbcstret").text

                    st.write("Chave da Nota:", chave)
                    st.write("Item da Nota:", item)
                    st.write("Data de Emissão da Nota:", data_emissao)
                    st.write("CFOP:", cfop)
                    st.write("NCM:", ncm)
                    st.write("Código do Produto:", codigo_produto)
                    st.write("Descrição da Nota:", descricao)
                    st.write("Quantidade:", quantidade)
                    st.write("cEAN:", cean)
                    st.write("vProd:", vprod)
                    st.write("ICMS vBCST:", icms_vbcst)
                    st.write("ICMS vBCSTRet:", icms_vbcstret)

                    st.markdown("---")

            except Exception as e:
                st.error(f"Erro ao processar o arquivo XML: {e}")