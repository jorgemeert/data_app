Readme · MD

# 📁 Conversor de Arquivos

Trabalho de Python desenvolvido em grupo, com o objetivo de praticar manipulação de dados e desenvolvimento de interfaces web simples com Python.

## 👥 Autores

- Jorge Meert
- Vinicius Henrique
- Gabriel Donato

## 📝 Sobre o projeto

Aplicação web simples que permite converter arquivos entre os formatos **CSV**, **XLSX**, **JSON** e **Parquet**. O usuário sobe um arquivo, escolhe o formato de saída desejado, visualiza os dados convertidos em uma tabela e baixa o resultado.

## 🚀 Tecnologias utilizadas

- **[Streamlit](https://streamlit.io/)** — construção da interface web
- **[Pandas](https://pandas.pydata.org/)** — leitura, conversão e manipulação dos dados
- **[Pathlib](https://docs.python.org/3/library/pathlib.html)** — manipulação de nomes e extensões de arquivo

## ▶️ Como executar

1. Instale as dependências:

```bash
   pip install streamlit pandas openpyxl pyarrow
```

2. Rode a aplicação:

```bash
   streamlit run app.py
```

3. Acesse o endereço mostrado no terminal (geralmente `http://localhost:8501`)

## 🔄 Formatos suportados

| Formato | Leitura | Escrita |
| ------- | :-----: | :-----: |
| CSV     |   ✅    |   ✅    |
| XLSX    |   ✅    |   ✅    |
| JSON    |   ✅    |   ✅    |
| Parquet |   ✅    |   ✅    |

## 📌 Como usar

1. Selecione o formato de saída desejado
2. Faça o upload do arquivo que deseja converter
3. Clique em **Converter**
4. Visualize a tabela com os dados
5. Clique em **Baixar arquivo** para salvar o resultado convertido
