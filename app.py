import streamlit as st
import pandas as pd

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
    "NLP": nlp_df,
    "AI": ai_df,
    "Math": math_df
}

# Set page title and page layout
st.set_page_config(page_title="Dork's Data Digest", page_icon=":books:", layout="wide")

# Define the UI layout
st.title("Dork's Data Digest")

# Display buttons for each cluster in the main area
col1, col2, col3 = st.columns(3)
for topic, df_cluster in dfs.items():
    if topic in ["Data Analysis", "Machine Learning", "Deep Learning"]:
        col1.button(topic, key=topic)
    elif topic in ["Computer Vision", "NLP", "AI"]:
        col2.button(topic, key=topic)
    else:
        col3.button(topic, key=topic)

# Display the selected cluster
selected_cluster = st.session_state.clicked_button or "Data Analysis"
st.subheader(f"Cluster: {selected_cluster}")
st.write(dfs[selected_cluster])
