import json 
import pandas as pd


dados_dict = {
    "nome" : ["Ana","Bruno","Carla"],
    "idade": [25,30,22],
    "cidade" : ["São Paulo", "Rio de Janeiro", "Curitiba"]
}

with open('json_data.json','w',encoding='utf-8') as file:
    json.dump(dados_dict,file,ensure_ascii=False,indent=4)



with open('json_data.json','r',encoding='utf-8') as file:
    dados_python = json.load(file)


#Abordagem A:

df_opcao_a = pd.DataFrame(dados_python)

# print(df_opcao_a)

#Abordagem B: read_json

df_opcao_b = pd.read_json('json_data.json')

# print(df_opcao_b)

#Transformando em CSV
df_opcao_b.to_csv('usuario.csv', index=False, encoding='utf-8')

#CSV PARA JSON

dados = {
    "id": [1,2,3],
    "nome" : ["Bruno","Silvio","Carla"],
    "cargo" : ["Analista" , "Desenvolvedor", "Gerente"],
    "salario" : [4500,6200,9500]
}


df_original = pd.DataFrame(dados)

print(df_original)

df_original.to_csv("dados.csv",index=False,encoding='utf-8')


df_original.to_json(
    "dados_output.json",
    orient='records',
    indent=4,
    force_ascii=False
)

df_original.to_json(
    "dados_output2.json",
    orient='columns',
    indent=4,
    force_ascii=False
)


df_original.to_json(
    "dados_output3.json",
    orient='table',
    indent=4,
    force_ascii=False
)