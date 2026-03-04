import streamlit as st
import pandas as pd
import preprocessor, helper
from helper import medal_tally

df = preprocessor.preprocess()

st.sidebar.title("Olympics Analysis")

user_menue = st.sidebar.radio(
    "Select an Option",
    ("Medal Tally", "Overall Analysis", "Country-wise-Analysis", "Athlete wise Analysis")
)

if user_menue == "Medal Tally":
    st.sidebar.header("Medal Tally")
    years, country = helper.country_year_list(df)

    selected_year = st.sidebar.selectbox("Select Year", years)
    selected_country = st.sidebar.selectbox("Select Country", country)

    medal_tally = helper.fetch_medal_tally(df, selected_year, selected_country)
    if selected_year == "Overall" and selected_country == "Overall":
        st.title("Overall Tally")
    if selected_year == "Overall" and selected_country == "Overall":

        st.dataframe(medal_tally)