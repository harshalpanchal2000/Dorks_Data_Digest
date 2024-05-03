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

# Define functions for each cluster page
def data_analysis_page():
    st.title("Data Analysis Cluster Page")
    st.write(dfs["Data Analysis"])

def machine_learning_page():
    st.title("Machine Learning Cluster Page")
    st.write(dfs["Machine Learning"])

def deep_learning_page():
    st.title("Deep Learning Cluster Page")
    st.write(dfs["Deep Learning"])

def computer_vision_page():
    st.title("Computer Vision Cluster Page")
    st.write(dfs["Computer Vision"])

def nlp_page():
    st.title("Natural Language Processing Cluster Page")
    st.write(dfs["Natural Language Processing"])

def ai_page():
    st.title("Artificial Intelligence Cluster Page")
    st.write(dfs["Artificial Intelligence"])

def math_page():
    st.title("Mathematics Cluster Page")
    st.write(dfs["Mathematics"])

# Define the homepage layout
def display_homepage():
    st.title("📖 Dork's Data Digest")
    st.subheader("Discover top-rated books based for Data Science")

# Run the app
def main():
    display_homepage()

    # Add links to cluster pages with emoticons in three columns
    st.write("Select your cluster page:")
    clusters = list(dfs.keys())
    num_clusters = len(clusters)
    num_columns = 3
    clusters_per_column = num_clusters // num_columns
    for i in range(num_columns):
        with st.sidebar:
            column_clusters = clusters[i * clusters_per_column: (i + 1) * clusters_per_column]
            for cluster in column_clusters:
                if st.button(cluster):
                    globals()[cluster.lower().replace(" ", "_") + "_page"]()

if __name__ == "__main__":
    main()
