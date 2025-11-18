import streamlit as st 
import pandas as pd
import joblib 

# Carregar dados e colocar no cache do Streamlit

@st.cache_data
def carregar_dados():
    return pd.read_csv('.\datasets\clusterizacao_laptops.csv')

df = carregar_dados()

# Sidebar para filtro
st.sidebar.header("Filtros")

# Selecionar modelos
model = st.sidebar.selectbox('Selecionar modelo', df['model'].unique())

# Filtrar modelo 
df_laptops_modelo = df[df['model'] == model]

# Filtar cluster do modelo escolhido
df_laptops_final = df[df['cluster'] == df_laptops_modelo.iloc[0]['cluster']]

# Vusualizar modelos
st.write('Recomendaçãoes de Modelo')
st.table(df_laptops_final)

# bash -> streamlit run app.py