import streamlit as st
import pandas as pd

def math_page():
    st.title("Mathematics Books")
    st.subheader("Discover top-rated books for Mathematics")
    
    # Load data
    math_books_df = pd.read_csv('datasets/Math.csv')
    
    # Display data
    st.write(math_books_df)
