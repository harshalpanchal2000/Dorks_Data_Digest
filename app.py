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
    "Natural Language Processing": nlp_df,
    "Artificial Intelligence": ai_df,
    "Mathematics": math_df
}

# Set page title and page layout
st.set_page_config(page_title="📚 Dork's Data Digest", page_icon=":books:", layout="wide")

# Define the UI layout
st.markdown("<h1 style='text-align: center;'>Dork's Data Digest</h1>", unsafe_allow_html=True)
st.markdown("<h3 style='text-align: center;'>Discover top-rated books based for Data Science</h3>", unsafe_allow_html=True)

# Display buttons for each cluster in the main area
col1, col2, col3 = st.columns(3)
selected_cluster = None
cluster_emoticons = {
    "Data Analysis": "📊",
    "Machine Learning": "🤖",
    "Deep Learning": "🧠",
    "Computer Vision": "📷",
    "Natural Language Processing": "💬",
    "Artificial Intelligence": "🚀",
    "Mathematics": "🔢"
}
for topic, df_cluster in dfs.items():
    if topic in ["Data Analysis", "Machine Learning", "Deep Learning"]:
        if col1.button(f"{cluster_emoticons[topic]} {topic}"):
            selected_cluster = topic
    elif topic in ["Computer Vision", "Natural Language Processing", "Artificial Intelligence"]:
        if col2.button(f"{cluster_emoticons[topic]} {topic}"):
            selected_cluster = topic
    else:
        if col3.button(f"{cluster_emoticons[topic]} {topic}"):
            selected_cluster = topic

# Display the selected cluster if it's not None
if selected_cluster is not None:
    st.subheader(f"Cluster: **{selected_cluster}**")
    st.write(dfs[selected_cluster])
