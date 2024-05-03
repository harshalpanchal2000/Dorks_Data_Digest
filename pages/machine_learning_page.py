import streamlit as st
import pandas as pd

def machine_learning_page():
    st.title("Machine Learning Books")
    st.subheader("Discover top-rated books for Machine Learning")
    
    # Load data
    machine_learning_books_df = pd.read_csv('datasets/Machine Learning.csv')
    
    # Display data
    st.write(machine_learning_books_df)
