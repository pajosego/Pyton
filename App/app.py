# importar bibliotecas
import streamlit as st
import pansas as pd
import numpy as np

#criar titulo utilizando a biblioteca streamlit
st.title("Web App Soccer Data")

#criar o sidebar utilizando a biblioteca streamlit
st.sidebar.header("Leagues")

st.sidebar.header("Season")

# WebScraping do Foottball Data, reunir informação dos csvs do site para fazer a base de dados: https://www.football-data.co.uk/mmz4281/2223/EO.csv //excel com a data da season 2023//
# criar uma função para altearar as Leagues a e seasons de acordo com a nossa seleção que fizermos nos sidbars, 
# def = cria a função
# load_data = nome da função
      
def load_data(league, season): 
    url =  "https://www.football-data.co.uk/mmz4281/" +season+ "/" +league+ ".csv"

#para ler a função, utiliza-se biblioteca pandas criando uma variavel data

data = pd.read_csv(url)
return data

# data frame




