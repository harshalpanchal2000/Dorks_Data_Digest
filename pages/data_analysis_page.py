import streamlit as st
import pandas as pd

def data_analysis_page():
    st.title("Data Analysis Books")
    st.subheader("Discover top-rated books for Data Analysis")
    
    # Load data
    data_analysis_books_df = pd.read_csv("https://github.com/harshalpanchal2000/whatshouldiread/blob/main/datasets/data_analysis.csv")
    
    # Display data
    st.write(data_analysis_books_df)
