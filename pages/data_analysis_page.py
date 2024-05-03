import streamlit as st
import pandas as pd

def data_analysis_page():
    st.title("Data Analysis Cluster Page")
    data_analysis_df = pd.read_csv('datasets/Data Analysis.csv')
    st.write(data_analysis_df)

if __name__ == "__main__":
    data_analysis_page()
