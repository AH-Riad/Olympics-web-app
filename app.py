import streamlit as st
import pandas as pd
import preprocessor, helper
from helper import medal_tally
import plotly.express as px
import matplotlib.pyplot as plt
import seaborn as sns

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

    if selected_year != "Overall" and selected_country == "Overall":
        st.title("Medal Tally in "+ str(selected_year)+ " Olympics")

    if selected_year == "Overall" and selected_country != "Overall":
        st.title(selected_country + " overall performance")

    if selected_year != "Overall" and selected_country != "Overall":
        st.title(selected_country + " performance in " + str(selected_year) + " Olympics")

    st.table(medal_tally)

if user_menue == "Overall Analysis":
    editions = df["Year"].unique().shape[0]-1
    cities = df["City"].unique().shape[0]
    sports = df["Sport"].unique().shape[0]
    events = df["Event"].unique().shape[0]
    athletes = df["Name"].unique().shape[0]
    nations = df["region"].unique().shape[0]

    col1, col2, col3 = st.columns(3)
    with col1:
        st.header("Editions")
        st.title(editions)
    with col2:
        st.header("Hosts")
        st.title(cities)
    with col3:
        st.header("Sports")
        st.title(sports)

    col1, col2, col3 = st.columns(3)
    with col1:
        st.header("Events")
        st.title(events)
    with col2:
        st.header("Nations")
        st.title(nations)
    with col3:
        st.header("Athletes")
        st.title(athletes)

    # ---------------------------
    # All graphs are now inside this block
    # ---------------------------
    nations_over_time = helper.data_over_time(df, 'region')
    fig = px.line(nations_over_time, x="Edition", y="region")
    st.title("Participating Nations Over Time")
    st.plotly_chart(fig)

    events_over_time = helper.data_over_time(df, 'Event')
    fig = px.line(events_over_time, x="Edition", y="Event")
    st.title("Events Over Time")
    st.plotly_chart(fig)

    athletes_over_time = helper.data_over_time(df, 'Name')
    fig = px.line(athletes_over_time, x="Edition", y="Name")
    st.title("Athletes Over Time")
    st.plotly_chart(fig)

    st.title("No. of Events over time(Every Sport)")
    fig, ax = plt.subplots(figsize=(20, 20))
    x = df.drop_duplicates(['Year', 'Sport', 'Event'])

    sns.heatmap(
        x.pivot_table(
            index="Sport",
            columns="Year",
            values="Event",
            aggfunc="count"
        ).fillna(0).astype(int),
        annot=True
    )
    st.pyplot(fig)

    st.title("Most Successful Athletes")
    sports_list = df['Sport'].unique().tolist()
    sports_list.sort()
    sports_list.insert(0, 'Overall')

    selected_sports = st.selectbox("Select Sport", sports_list)

    x = helper.most_successful(df, selected_sports)
    st.table(x)