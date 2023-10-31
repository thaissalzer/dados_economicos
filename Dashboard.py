import streamlit as st
import requests
import pandas as pd
import plotly.express as px

#inserindo o titulo
st.title('Indicadores Econômicos')
st.title('Dados do :blue[BACEN] 💰💵')

#dados
url = 'https://api.bcb.gov.br/dados/serie/bcdata.sgs.433/dados?formato=json'
response = requests.get(url)
dados = pd.DataFrame.from_dict(response.json())
dados['data'] = pd.to_datetime(dados['data'], format='%d/%m/%Y')
dados['valor'] = dados['valor'].astype(float)

# inserindo uma métrica (média de inflação)

st.metric('IPCA médio', f"{dados['valor'].mean():.2f}")
data_mais_recente = dados['data'].max()  # Obtendo a data mais recente

# Formatando a data como uma string no formato desejado (por exemplo, 'dd/mm/yyyy')
data_formatada = data_mais_recente.strftime('%d/%m/%Y')

# Exibindo a data formatada no Streamlit
st.metric('Data mais recente', data_formatada)

# Filtrando os dados para obter o IPCA mais recente
ipca_mais_recente = dados[dados['data'] == dados['data'].max()]['valor'].values[0]

# Exibindo o IPCA mais recente formatado com duas casas decimais
st.metric('IPCA mais recente', f"{ipca_mais_recente:.2f}")


st.dataframe(dados)