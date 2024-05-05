import streamlit as st
from pages.data_analysis_page import data_analysis_page
from pages.machine_learning_page import machine_learning_page
from pages.deep_learning_page import deep_learning_page
from pages.computer_vision_page import computer_vision_page
from pages.nlp_page import nlp_page
from pages.ai_page import ai_page
from pages.math_page import math_page


# Set page title and page layout
st.set_page_config(
    page_title="Dork's Data Digest - Discover top-rated books based on Data Science topics",
    page_icon=":books:",
    layout="wide"
)

# Define a function to display the selected page
def display_page(page):
    if page == "Data Analysis":
        data_analysis_page()
    elif page == "Machine Learning":
        machine_learning_page()
    elif page == "Deep Learning":
        deep_learning_page()
    elif page == "Computer Vision":
        computer_vision_page()
    elif page == "Natural Language Processing":
        nlp_page()
    elif page == "Artificial Intelligence":
        ai_page()
    elif page == "Mathematics":
        math_page()

# Define the homepage layout
def display_homepage():
    st.markdown(
        "<h1 style='text-align: center;'>📖 Dork's Data Digest</h1>"
        "<h3 style='text-align: center;'>Discover top-rated books based for Data Science</h3>"
        "<p style='text-align: center;'>Select your cluster page:</p>",
        unsafe_allow_html=True
    )

    clusters = [
        ("Data Analysis", "📊"),
        ("Machine Learning", "🤖"),
        ("Deep Learning", "🧠"),
        ("Computer Vision", "👁️"),
        ("Natural Language Processing", "🗣️"),
        ("Artificial Intelligence", "✨"),  # Changed emoticon for AI
        ("Mathematics", "🧮")
    ]

    col1, col2, col3 = st.columns(3)

    for i, (cluster, icon) in enumerate(clusters):
        if i % 3 == 0:
            button_col = col1
        elif i % 3 == 1:
            button_col = col2
        else:
            button_col = col3
        
        if button_col.button(f"{icon} {cluster}", key=f"{cluster}_button"):
            display_page(cluster)

    st.markdown(
        "<div style='position: fixed; bottom: 20px; width: 100%; text-align: left; padding-left: 40%;'>"
        "<p>Built by <a href='https://www.linkedin.com/in/harshal-panchal/' target='_blank'>Harshal Panchal</a></p>"
        "</div>",
        unsafe_allow_html=True
    )

# Run the app
def main():
    display_homepage()

with st.sidebar():
    # Leave this empty to hide the sidebar for this portion of the app
    pass

if __name__ == "__main__":
    main()
