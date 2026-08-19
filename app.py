import streamlit as st
import pandas as pd
import json
import os

st.title("Bem vindo ao nosso conversor de arquivos")

formato = st.selectbox("Digite o formato do arquivo que você deseja converter",['CSV','Parquet','XLSX','JSON'])
arquivo = st.file_uploader("Coloque aqui o arquivo que deseja converter")


if st.button("Converter"):
    if arquivo and formato:
        nome_arquivo = os.path.basename(arquivo)
        if formato == 'CSV':
            if '.xlsx' in nome_arquivo:
                print('é de csv para xlxs')