import streamlit as st
import pandas as pd
from multipage import MultiPage

# Load the DataFrame from CSV files
data_analysis_df = pd.read_csv('datasets/Data Analysis.csv')
machine_learning_df = pd.read_csv('datasets/Machine Learning.csv')
deep_learning_df = pd.read_csv('datasets/Deep Learning.csv')
computer_vision_df = pd.read_csv('datasets/Computer Vision.csv')
nlp_df = pd.read_csv('datasets/NLP.csv')
ai_df = pd.read_csv('datasets/AI.csv')
math_df = pd.read_csv('datasets/Math.csv')

# Create a dictionary to store DataFrames
dfs = {
    "Data Analysis": data_analysis_df,
    "Machine Learning": machine_learning_df,
    "Deep Learning": deep_learning_df,
    "Computer Vision": computer_vision_df,
    "Natural Language Processing": nlp_df,
    "Artificial Intelligence": ai_df,
    "Mathematics": math_df
}

# Define the UI layout
def display_homepage():
    st.title("Dork's Data Digest")
    st.subheader("Discover top-rated books based for Data Science")
    for cluster in dfs.keys():
        if st.button(cluster):
            session_state = get_session_state()
            session_state.selected_cluster = cluster
            st.experimental_rerun()

# Define your page functions
def home():
    display_homepage()

def cluster_page(cluster_name):
    st.title(f"{cluster_name} Cluster Page")
    st.write(dfs[cluster_name])

# Create an instance of the MultiPage class
app = MultiPage()

# Add your pages to the app
app.add_page("Home", home)
for cluster in dfs.keys():
    app.add_page(cluster, lambda: cluster_page(cluster))

# Run the app
app.run()
