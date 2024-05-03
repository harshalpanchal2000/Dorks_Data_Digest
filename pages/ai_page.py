import streamlit as st
import pandas as pd

def ai_page():
    st.title("Artificial Intelligence Books")
    st.subheader("Discover top-rated books for Artificial Intelligence")
    
    # Load data
    ai_books_df = pd.read_csv('datasets/AI.csv')
    
    # Display data
    st.write(ai_books_df)
