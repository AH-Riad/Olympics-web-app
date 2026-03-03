import streamlit as st
import pandas as pd
import preprocessor, helper
from helper import medal_tally

df = preprocessor.preprocess()

user_menue = st.sidebar.radio(
    "Select an Option",
    ("Medal Tally", "Overall Analysis", "Country-wise-Analysis", "Athlete wise Analysis")
)

st.dataframe(df.head())

if user_menue == "Medal Tally":
    medal_tally = helper.medal_tally(df)
    st.dataframe(medal_tally)