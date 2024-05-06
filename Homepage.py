import streamlit as st

# Define the homepage layout
def display_homepage():
    st.markdown(
        "<h1 style='text-align: center;'>📖 Dork's Data Digest</h1>"
        "<h3 style='text-align: center;'>Discover top-rated books based for Data Science</h3>",
        unsafe_allow_html=True
    )


    st.markdown(
        "<div style='position: fixed; bottom: 20px; width: 100%; text-align: left; padding-left: 40%;'>"
        "<p>Built by <a href='https://www.linkedin.com/in/harshal-panchal/' target='_blank'>Harshal Panchal</a></p>"
        "</div>",
        unsafe_allow_html=True
    )

# Run the app
def main():
    display_homepage()

if __name__ == "__main__":
    main()
