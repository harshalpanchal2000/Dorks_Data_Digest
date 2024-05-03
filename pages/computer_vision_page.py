import streamlit as st
import pandas as pd

def computer_vision_page():
    st.title("Computer Vision Books")
    st.subheader("Discover top-rated books for Computer Vision")
    
    # Load data
    computer_vision_books_df = pd.read_csv('datasets/Computer Vision.csv')
    
    # Display data
    st.write(computer_vision_books_df)
