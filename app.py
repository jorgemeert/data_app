import streamlit as st
import pandas as pd
import json
from pathlib import Path


def converter(arquivo,formato): 
      if arquivo and formato:
            nome = Path(arquivo.name.lower())
            if nome.suffix == '.xlsx':
                df = pd.read_excel(arquivo)
            elif nome.suffix == '.csv':
                df = pd.read_csv(arquivo)
            elif nome.suffix == '.parquet':
                df = pd.read_parquet(arquivo)
            elif nome.suffix == '.json':
                df = pd.read_json(arquivo)    

            if formato == 'CSV':
                df.to_csv(f'{nome.stem}.csv',index=False)
                destino = f'{nome.stem}.csv'
            elif formato == 'XLSX':
                df.to_excel(f'{nome.stem}.xlsx', index=False)
                destino = f'{nome.stem}.xlsx'
            elif formato ==  'Parquet':
                df.to_parquet(f'{nome.stem}.parquet')
                destino = f'{nome.stem}.parquet'
            else:
                df.to_json(f'{nome.stem}.json')
                destino = f'{nome.stem}.json'
                    
            with open(destino,'rb') as f:
                data = f.read()

            if '.csv' in destino:
                mime = "text/csv"
            elif '.xlsx' in destino:
                mime = "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
            elif '.json' in destino:
                mime = "application/json"    
            else:
                mime = "application/octet-stream"
            
            return mime,destino,data,df
                   

st.title("Bem vindo ao nosso conversor de arquivos")

formato = st.selectbox("Selecione o formato que deseja converter o arquivo",['CSV','Parquet','XLSX','JSON'])
arquivo = st.file_uploader("Coloque aqui o arquivo que deseja converter")


if st.button('Converter'):
    if arquivo and formato:
       try: 
            mime,destino,data,df = converter(arquivo,formato)
            if mime and destino and data:
                st.dataframe(df)
                st.download_button(
                    label="Baixar arquivo",
                    data=data,
                    file_name=destino,
                    mime= mime
                )
        
       except Exception as e:
            st.markdown('O arquivo que você colocou não é possíveL ser convertido, tente selecionar um arquivo tipo : **(CSV,JSON,PARQUET,XLSX)**')   
            

 
    
