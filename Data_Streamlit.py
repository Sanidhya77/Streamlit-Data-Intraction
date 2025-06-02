import streamlit as st

import pandas as pd

st.title("Types of Games sold In US Cities")
file= st.file_uploader("Upload your sales data", type=["csv"])


if file:
    df = pd.read_csv(file)
    st.subheader("Data Preview")
    st.dataframe(df)


if file:
    st.subheader("Sales Summary")
    st.write(df.describe())   

if file:
    City= df["City"].unique()
    selected_city = st.selectbox("Select by city", City)    
    filtered_data= df[df["City"] == selected_city]
    st.dataframe(filtered_data)import streamlit as st

import pandas as pd

st.title("Types of Games sold In US Cities")
file= st.file_uploader("Upload your sales data", type=["csv"])


if file:
    df = pd.read_csv(file)
    st.subheader("Data Preview")
    st.dataframe(df)


if file:
    st.subheader("Sales Summary")
    st.write(df.describe())   

if file:
    City= df["City"].unique()
    selected_city = st.selectbox("Select by city", City)    
    filtered_data= df[df["City"] == selected_city]
    st.dataframe(filtered_data)
