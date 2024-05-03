import streamlit as st
import pandas as pd

def deep_learning_page():
    st.title("Deep Learning Books")
    st.subheader("Discover top-rated books for Deep Learning")
    
    # Load data
    deep_learning_books_df = pd.read_csv('datasets/Deep Learning.csv')
    
    # Display data
    st.write(deep_learning_books_df)

if __name__ == "__main__":
    deep_learning_page()
