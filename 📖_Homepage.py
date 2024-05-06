import streamlit as st

# Define the homepage layout
def display_homepage():
    st.markdown(
        "<h1 style='text-align: center;'>📖 Dork's Data Digest</h1>"
        "<h3 style='text-align: center;'>Discover top-rated books based for Data Science</h3>",
        unsafe_allow_html=True
    )

    st.markdown("""
        <p style='text-align:center;'>This is your data science book recommendation app, where you will find top-rated books related to Data Science. 
        Whether you're interested in Data Analysis, Machine Learning, Deep Learning, Computer Vision, Natural Language Processing, Artificial Intelligence, or Mathematics, 
        we've got you covered! Simply select the type of book you'd like from the sidebar.</p>
        """,
        unsafe_allow_html=True
    )

    st.markdown(
        "<div style='position: fixed; bottom: 20px; width: 100%; text-align: left; padding-left: 17%;'>"
        "<p>Built by <a href='https://www.linkedin.com/in/harshal-panchal/' target='_blank'>Harshal Panchal</a></p>"
        "</div>",
        unsafe_allow_html=True
    )

# Run the app
def main():
    st.set_page_config(page_title="Dork's Data Digest", page_icon="📖")
    display_homepage()

if __name__ == "__main__":
    main()
