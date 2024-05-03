import streamlit as st
import pandas as pd

def machine_learning_page():
    st.title("Best Machine Learning Books")
    machine_learning_df = pd.read_csv('datasets/Machine Learning.csv')
    st.write(machine_learning_df)

if __name__ == "__main__":
    machine_learning_page()
