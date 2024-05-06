import streamlit as st
from pages import data_analysis_page, machine_learning_page, deep_learning_page, computer_vision_page, nlp_page, ai_page, math_page

# Define the homepage layout
def display_homepage():
    st.markdown(
        "<h1 style='text-align: center;'>📖 Dork's Data Digest</h1>"
        "<h3 style='text-align: center;'>Discover top-rated books based for Data Science</h3>",
        unsafe_allow_html=True
    )

    clusters = [
        ("Data Analysis", "📊", data_analysis_page),
        ("Machine Learning", "🤖", machine_learning_page),
        ("Deep Learning", "🧠", deep_learning_page),
        ("Computer Vision", "👁️", computer_vision_page),
        ("Natural Language Processing", "🗣️", nlp_page),
        ("Artificial Intelligence", "✨", ai_page),
        ("Mathematics", "🧮", math_page)
    ]

    col1, col2, col3 = st.columns(3)

    for cluster, icon, page in clusters:
        if col1.button(f"{icon} {cluster}", key=f"{cluster}_button"):
            st.experimental_set_query_params(page=cluster)

    st.markdown(
        "<div style='position: fixed; bottom: 20px; width: 100%; text-align: left; padding-left: 40%;'>"
        "<p>Built by <a href='https://www.linkedin.com/in/harshal-panchal/' target='_blank'>Harshal Panchal</a></p>"
        "</div>",
        unsafe_allow_html=True
    )

# Run the app
def main():
    display_homepage()

    # Check for page parameter in the URL and display the corresponding page
    page = st.experimental_get_query_params().get("page", None)
    if page:
        if page == "Data Analysis":
            data_analysis_page.main()
        elif page == "Machine Learning":
            machine_learning_page.main()
        elif page == "Deep Learning":
            deep_learning_page.main()
        elif page == "Computer Vision":
            computer_vision_page.computer_vision_page()
        elif page == "Natural Language Processing":
            nlp_page.main()
        elif page == "Artificial Intelligence":
            ai_page.main()
        elif page == "Mathematics":
            math_page.main()

if __name__ == "__main__":
    main()
