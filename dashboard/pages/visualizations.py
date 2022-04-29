# streamlit_app.py

import streamlit as st
import mysql.connector
import pandas as pd
import numpy as np
import os
import plotly.graph_objects as go




# from dashboard.pages.dashboard import DATA_URL

# Initialize connection.
# Uses st.experimental_singleton to only run once.
@st.experimental_singleton
def init_connection():
    return mysql.connector.connect(**st.secrets["mysql"])

conn = init_connection()

# Perform query.
# Uses st.experimental_memo to only rerun when the query changes or after 10 min.
@st.experimental_memo(ttl=600)
@st.cache
def run_query(query):
    with conn.cursor() as cur:
        cur.execute(query)
        return cur.fetchall()


# DATA_URL = "../data/processed_tweet_data.csv"

@st.cache
def load_data(DATA_URL):
    data = pd.read_csv(DATA_URL)
    return data
print(os.getcwd())


def app():
    # with st.container():
    #     st.title("This is a visualization of the most common words in the Dataset")
    #     df = load_data("../data/cleaned_tweet_data.csv")

    #     flattened_words_df = pd.DataFrame(
    #         [word for words_list in df.clean_text
    #         for word in words_list.split(' ')],
    #         columns=['word'])

    #     flattened_words_df
                
    #     # common_hashtags = flattened_hashtags_df.hashtag.value_counts()[1:21]
    #     # print(common_hashtags)
    #     st.dataframe(flattened_words_df)
    #     # You can call any Streamlit command, including custom components:
    #     # st.bar_chart(np.random.randn(50, 3))



    with st.container():
        st.title("This is a visualization of the languages in the Dataset")

        data = load_data("../data/processed_tweet_data.csv")
        lang = data['lang'].value_counts()


        st.bar_chart(lang)
       