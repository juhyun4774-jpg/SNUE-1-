import streamlit as st
import pandas as pd
import numpy as np

st.title('My first stramlit app')
st.write("Here's our first attempt at using data to create a table:")
st.write(pd.DataFrame({
    'first column': [1, 2, 3, 4],
    'second column': [10, 20, 30, 40]
}))

st.write("Streamlit supports a wide range of data visualizations, including [Plotly, Altair, and Bokeh charts](https://docs.streamlit.io/develop/api-reference/charts). 📊 And with over 20 input widgets, you can easily make your data interactive!")

all_users = ["korea", "japan", "China"]
with st.container(border=True):
    users = st.multiselect("Users", all_users, default=all_users)
    rolling_average = st.toggle("snue")

np.random.seed(42)
data = pd.DataFrame(np.random.randn(50, len(users)), columns=users)
if rolling_average:
    data = data.rolling(5).mean().dropna()

tab1, tab2 = st.tabs(["Chart", "Dataframe"])
tab1.line_chart(data, height=200)
tab2.dataframe(data, height=200, use_container_width=True)









