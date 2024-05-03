import streamlit as st
import pandas as pd

def data_analysis_page():
    st.title("Data Analysis Books")
    st.subheader("Discover top-rated books for Data Analysis")
    
    # Load data
    data_analysis_books_df = pd.read_csv('datasets/Data Analysis Books.csv')
    
    # Display data
    st.write(data_analysis_books_df)
