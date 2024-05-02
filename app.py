import streamlit as st
import pandas as pd

# Set page title and page layout
st.set_page_config(
    page_title="Dork's Data Digest - Discover top-rated books based on Data Science topics",
    page_icon=":books:",
    layout="wide"
)

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
    st.markdown("<h1 style='text-align: center;'>📖 Dork's Data Digest</h1>", unsafe_allow_html=True)
    st.markdown("<h3 style='text-align: center;'>Discover top-rated books based for Data Science</h3>", unsafe_allow_html=True)
    
    num_clusters = len(dfs)
    clusters_per_column = (num_clusters + 2) // 3  # Calculate clusters per column with rounding up
    
    col1, col2, col3 = st.columns(3)  # Create three columns
    
    clusters = list(dfs.keys())
    for i, cluster in enumerate(clusters):
        if i < clusters_per_column:
            col1.button(cluster)
        elif i < 2 * clusters_per_column:
            col2.button(cluster)
        else:
            col3.button(cluster)

# Define your page functions
def home():
    display_homepage()

def cluster_page(cluster_name):
    st.title(f"{cluster_name} Cluster Page")
    st.write(dfs[cluster_name])

# Run the app
home()
