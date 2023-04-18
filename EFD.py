import os
import csv
import streamlit as st


def remover_fator_conversao(linhas_efd):
    """Remove a linha com o registro |0220| do arquivo EFD."""
    novas_linhas = []
    for linha in linhas_efd:
        if not linha.startswith("|0220|"):
            novas_linhas.append(linha)
    return novas_linhas


def main():
    # Parte 1: Remover fator de conversão
    st.header("Remover fator de conversão")
    uploaded_file = st.file_uploader("Escolha um arquivo de texto", type=["txt"])
    if uploaded_file is not None:
        file_contents = uploaded_file.read().decode("utf-8")
        linhas_efd = file_contents.splitlines()
        novas_linhas = remover_fator_conversao(linhas_efd)
        st.download_button(
            label="Download do arquivo sem fator de conversão",
            data="\n".join(novas_linhas),
            file_name="sem_fator.txt",
            mime="text/plain",
        )
def alterar_codigo_produto(linhas_efd, codigo_preservado, codigos_convertidos):
    """Altera o código do produto nos registros C170, 0200 e H010."""
    novas_linhas = []
    for linha in linhas_efd:
        campos = linha.split("|")
        if len(campos) > 3 and campos[1] == "C170":
            codigo_produto = campos[3]
            for cp in codigo_preservado:
                if codigo_produto.startswith(cp):
                    # Mantém o código original se começa com a letra preservada
                    break
            else:
                codigo_produto = "".join(c for c in codigo_produto if c.isnumeric())
                codigo_produto = codigo_produto[-6:].lstrip("0")
                if campos[3][:-6] in codigos_convertidos:
                    codigo_produto = campos[3][:-6] + codigo_produto
            campos[3] = codigo_produto  # Remove os zeros à esquerda

        elif len(campos) > 2 and campos[1] in ["0200", "H010"]:
            codigo_produto = campos[2]
            for cp in codigo_preservado:
                if codigo_produto.startswith(cp):
                    # Mantém o código original se começa com a letra preservada
                    break
            else:
                codigo_produto = "".join(c for c in codigo_produto if c.isnumeric())
                codigo_produto = codigo_produto[-6:].lstrip("0")
                if campos[2][:-6] in codigos_convertidos:
                    codigo_produto = campos[2][:-6] + codigo_produto
            campos[2] = codigo_produto  # Remove os zeros à esquerda

        novas_linhas.append("|".join(campos))

    return novas_linhas


def main():
    # Parte 3: Alterar código do produto
    st.header("Alterar código do produto")
    uploaded_file = st.file_uploader("Escolha um arquivo de texto", type=["txt"])
    if uploaded_file is not None:
        file_contents = uploaded_file.read().decode("latin-1")
        linhas_efd = file_contents.splitlines()

        # Códigos que devem manter a letra no início
        codigo_preservado = [
            "PROIMPEXP",
            "PROMATESC",
            "PROMATHIG",
            "PROMATINF",
            "PROMATPRO",
            "PROBENPVA",
            "PRORECELE",
            "PROCONBEN",
        ]

        # Lista com os códigos que precisam ser convertidos
        codigos_convertidos = st.text_input(
            "Códigos que precisam ser convertidos (separados por vírgula)"
        ).split(",")

        novas_linhas = alterar_codigo_produto(
            linhas_efd, codigo_preservado, codigos_convertidos
        )
        st.download_button(
            label="Download do arquivo com códigos de produto alterados",
            data="\n".join(novas_linhas),
            file_name="com_codigos_alterados.txt",
            mime="text/plain",
            )
        

