
import streamlit as st

# Custom imports 
from multipage import MultiPage
# from pages import 
from pages import dashboard, visualizations

# Create an instance of the app 
app = MultiPage()

# Title of the main page
st.title("Twitter Data Analysis")

# Add all your applications (pages) here
app.add_page("Dashboard", dashboard.app)
app.add_page("Visualizations", visualizations.app)

# The main app
app.run()
