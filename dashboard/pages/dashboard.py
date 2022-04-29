import streamlit as st
import pandas as pd
import numpy as np



@st.cache
def load_data(DATA_URL):
    data = pd.read_csv(DATA_URL)
    return data

def app():
   
    with st.container():
        st.title("A table of the preprocessed Tweets")

        data = load_data("../data/cleaned_tweet_data.csv")

        cols = data.columns.tolist()
        st_ms = st.multiselect("Columns", cols, default=cols)
        st.dataframe(data[st_ms])



    