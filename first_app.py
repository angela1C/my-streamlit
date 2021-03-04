import streamlit as st
import numpy as np
import pandas as pd

st.title("My first app")
st.write("Creating a dataframe")
st.write(pd.DataFrame({'col_A': [1,2,3,4], 'colB': [10,20,30,40]}))

chart_data = pd.DataFrame(np.random.randn(20,3), columns = ['a','b','c'])
st.line_chart(chart_data)

"""
map_data = pd.DataFrame(
    np.random.randn(1000,2) / [50,50] + [37.76, -122.4], columns = ['lat','lon'])


st.map(map_data)
"""

if st.checkbox('Show dataframe'):
    chart_data = pd.DataFrame(np.random.randn(20,3), columns = ['a','b','c'])
    st.line_chart(chart_data)