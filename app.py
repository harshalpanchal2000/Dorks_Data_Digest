import streamlit as st
from pages import home_page, data_analysis_page, machine_learning_page, deep_learning_page, \
    computer_vision_page, nlp_page, ai_page, math_page

# Set page title and page layout
st.set_page_config(
    page_title="Dork's Data Digest - Discover top-rated books based on Data Science topics",
    page_icon=":books:",
    layout="wide"
)

# Define a function to display the selected page
def display_page(page):
    if page == "Home":
        home_page()
    elif page == "Data Analysis":
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
    st.title("📖 Dork's Data Digest")
    st.subheader("Discover top-rated books based for Data Science")
    st.write("Select your cluster page:")

    clusters = {
        "Data Analysis": "📊",
        "Machine Learning": "🤖",
        "Deep Learning": "🧠",
        "Computer Vision": "👁️",
        "Natural Language Processing": "🗣️",
        "Artificial Intelligence": "🧠",
        "Mathematics": "🧮"
    }

    col1, col2, col3 = st.columns(3)

    for cluster, icon in clusters.items():
        if col1.button(f"{icon} {cluster}"):
            display_page(cluster)
        elif col2.button(f"{icon} {cluster}"):
            display_page(cluster)
        elif col3.button(f"{icon} {cluster}"):
            display_page(cluster)

# Run the app
def main():
    display_homepage()

if __name__ == "__main__":
    main()
