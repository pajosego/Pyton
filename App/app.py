# importar bibliotecas
import streamlit as st
import pandas as pd
import numpy as np

#criar titulo utilizando a biblioteca streamlit
st.title("Web App Soccer Data")

#criar o sidebar utilizando a biblioteca streamlit
st.sidebar.header("Leagues")
selected_league = st.sidebar.selectbox('League' , [ 'England' ,  'Germany' ,  'Spain' ,  'Italy' ,  'France'] )

st.sidebar.header("Season")
selected_season = st.sidebar.selectbox ('Season' , ['2022/2021' , '2021/2020', '2020/2019'] )

# WebScraping do Foottball Data, reunir informação dos csvs do site para fazer a base de dados: https://www.football-data.co.uk/mmz4281/2223/EO.csv //excel com a data da season 2023//
# criar uma função para altearar as Leagues a e seasons de acordo com a nossa seleção que fizermos nos sidbars, 
# def = cria a função
# load_data = nome da função, funçao load_data serve para receber uma league e uma season para substituir na url esses campos
#para ler a função, utiliza-se a biblioteca pandas criando uma variavel data     


df = load_data(selected_league, selected_season)
# data frame
   
  if selected_league == 'Germany':
         league = 'D1'
  if selected_league == 'Italy':
         league = 'I1'
  if selected_league == 'Spain':
         league = 'SP1'
  if selected_league == 'France':
         league = 'F1'


if selected_season == '2021/2022':
      season = '2022'
if selected_season == '2020/2021':
      season = '2021'
if selected_season == '2019/2020':
      season = '2020'


def load_data(league, season): 
    url =  "https://www.football-data.co.uk/mmz4281/" +season+ "/" +league+ ".csv"
    data = pd.read_csv (url)
    return data

df = load_data(selected_league, selected_season)























