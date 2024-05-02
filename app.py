To create separate pages for each cluster, you can define a function for each cluster page. Here's how you can modify the code:

```python
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

# Run the app
selected_page = st.sidebar.selectbox("Select Page", ["Home", "Data Analysis", "Machine Learning", "Deep Learning", "Computer Vision", "Natural Language Processing", "Artificial Intelligence", "Mathematics"])

if selected_page == "Home":
    st.title("Home Page")
    st.write("Welcome to the home page!")
elif selected_page == "Data Analysis":
    data_analysis_page()
elif selected_page == "Machine Learning":
    machine_learning_page()
elif selected_page == "Deep Learning":
    deep_learning_page()
elif selected_page == "Computer Vision":
    computer_vision_page()
elif selected_page == "Natural Language Processing":
    nlp_page()
elif selected_page == "Artificial Intelligence":
    ai_page()
elif selected_page == "Mathematics":
    math_page()
``` 

With this code, each cluster page function is called when the corresponding cluster name is selected from the sidebar.
