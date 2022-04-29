# streamlit_app.py
#DB Connector

import streamlit as st
import mysql.connector
import pandas as pd

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

rows = run_query("SELECT * from TweetInformation;")

# Print results.
for row in rows:
    st.write(f"{row[0]} has a :{row[1]}:")

