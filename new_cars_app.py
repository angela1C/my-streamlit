import streamlit as st
import numpy as np
import pandas as pd


cars2020 = pd.read_csv("TEA28.20210303T230357.csv")
cars2020.head()

cars2020.drop(['Year','Statistic', 'UNIT'], axis=1, inplace=True)

st.title("New cars registered in 2020")

df=pd.DataFrame(cars2020)

dfsmall = df.sample(n=100)


st.area_chart(dfsmall)