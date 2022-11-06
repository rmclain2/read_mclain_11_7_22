import streamlit as st
import pandas as pd
import altair as alt
import numpy as np


#Import the Baseball HOF data set
HOF_data = pd.read_csv("2022_team_stats.csv")

st.write(HOF_data)

st.sidebar.header("Pick two variables for your scatter plot")
x_val=st.sidebar.selectbox("Pick your x-axis", HOF_data.select_dtypes(include=np.number).columns.tolist())
y_val=st.sidebar.selectbox("Pick your y-axis", HOF_data.select_dtypes(include=np.number).columns.tolist())


scatter = alt.Chart(HOF_data, title=f"Correlation between {x_val} and {y_val}").mark_point().encode(
    alt.X(x_val, title=f"{x_val}"),
    alt.Y(y_val, title=f"{y_val}"),
    tooltip=["Team",x_val, y_val])
st.altair_chart(scatter, use_container_width=True)

corr = round(HOF_data[x_val].corr(HOF_data[y_val]),2)
st.write(f"The correlation between {x_val} and {y_val} is {corr}")