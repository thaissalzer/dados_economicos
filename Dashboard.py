import streamlit as st
import requests
import pandas as pd
import plotly.express as px

# Inserindo o título
st.title('Indicadores Econômicos')
st.title('Dados do :blue[BACEN] 💰💵')

# Dados
url = 'https://api.bcb.gov.br/dados/serie/bcdata.sgs.433/dados?formato=json'
response = requests.get(url)
dados = pd.DataFrame.from_dict(response.json())
dados['data'] = pd.to_datetime(dados['data'], format='%d/%m/%Y')
dados['valor'] = dados['valor'].astype(float)

# Inserindo uma métrica (média de inflação)
data_mais_recente = dados['data'].max()  # Obtendo a data mais recente
data_formatada = data_mais_recente.strftime('%d/%m/%Y')

# Exibindo a data e o valor do IPCA mais recente
st.metric('Data mais recente', data_formatada)
ipca_mais_recente = dados[dados['data'] == data_mais_recente]['valor'].values[0]
st.metric('IPCA mais recente', f"{ipca_mais_recente:.2f}")

# Gráfico do IPCA total
st.subheader('Gráfico IPCA Total')
fig_total = px.line(dados, x='data', y='valor', title='IPCA Mensal')
fig_total.update_xaxes(title_text='Data', tickangle=45)
fig_total.update_yaxes(title_text='Valor')
st.plotly_chart(fig_total)

# Dividindo os dados
dados_antes_1995 = dados[dados['data'] < '1995-01-01']
dados_depois_1995 = dados[dados['data'] >= '1995-01-01']

# Gráfico IPCA antes de 1995
st.subheader('IPCA Antes de 1995')
fig_antes_1995 = px.line(dados_antes_1995, x='data', y='valor', title='IPCA Antes de 1995')
fig_antes_1995.update_xaxes(title_text='Data', tickangle=45)
fig_antes_1995.update_yaxes(title_text='Valor')
st.plotly_chart(fig_antes_1995)

# Gráfico IPCA depois de 1995
st.subheader('IPCA Depois de 1995')
fig_depois_1995 = px.line(dados_depois_1995, x='data', y='valor', title='IPCA Depois de 1995')
fig_depois_1995.update_xaxes(title_text='Data', tickangle=45)
fig_depois_1995.update_yaxes(title_text='Valor')
st.plotly_chart(fig_depois_1995)

# Exibindo o DataFrame completo
st.dataframe(dados)
