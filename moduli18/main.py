import pandas as pd
import streamlit as st
import plotly.express as px

books_df = pd.read_csv("bestsellers_with_categories_2022_03_27.csv")


st.header("Displaying dataframes")


data = pd.DataFrame({
    'Name': ['Dreni' , 'Gerti' , 'Deon'],
    'Age': ['16' , '15' , '16' ],
    'City': ['Prishtina' , 'Prizren' , 'Ferizaj']

})

st.dataframe(data)