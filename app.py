import streamlit as st
import pandas as pd

# Load the DataFrame from CSV files
data_analysis_df = pd.read_csv('datasets/Data Analysis.csv')
machine_learning_df = pd.read_csv('datasets/Machine Learning.csv')
deep_learning_df = pd.read_csv('datasets/Deep Learning.csv')
computer_vision_df = pd.read_csv('datasets/Computer Vision.csv')
nlp_df = pd.read_csv('datasets/NLP.csv')
ai_df = pd.read_csv('datasets/AI.csv')
math_df = pd.read_csv('datasets/Math.csv')

# Create a dictionary to store DataFrames
dfs = {
    "Data Analysis": data_analysis_df,
    "Machine Learning": machine_learning_df,
    "Deep Learning": deep_learning_df,
    "Computer Vision": computer_vision_df,
    "Natural Language Processing": nlp_df,
    "Artificial Intelligence": ai_df,
    "Mathematics": math_df
}

# Set page title and page layout
st.set_page_config(
    page_title="📖 Dork's Data Digest - Discover top-rated books based on Data Science topics",
    page_icon=":books:",
    layout="wide",
    initial_sidebar_state="expanded"  # Expand the sidebar by default
)

# Define the UI layout
st.markdown("<h1 style='text-align: center;'> 📖 Dork's Data Digest</h1>", unsafe_allow_html=True)
st.markdown("<div style='margin-bottom:20px;'></div>", unsafe_allow_html=True)  # Add space between title and subtitle
st.markdown("<h3 style='text-align: center; margin-bottom: 20px;'>Select a Data Science topic below to explore top-rated books:</h3>", unsafe_allow_html=True)

# Display buttons for each cluster in the main area
col1, col2, col3 = st.columns(3)
selected_cluster = None
cluster_emoticons = {
    "Data Analysis": "📊",
    "Machine Learning": "🤖",
    "Deep Learning": "🧠",
    "Computer Vision": "📷",
    "Natural Language Processing": "💬",
    "Artificial Intelligence": "🚀",
    "Mathematics": "🔢"
}
for topic, df_cluster in dfs.items():
    if topic in ["Data Analysis", "Machine Learning", "Deep Learning"]:
        if col1.button(f"{cluster_emoticons[topic]} {topic}"):
            selected_cluster = dfs[topic]
    elif topic in ["Computer Vision", "Natural Language Processing", "Artificial Intelligence"]:
        if col2.button(f"{cluster_emoticons[topic]} {topic}"):
            selected_cluster = dfs[topic]
    else:
        if col3.button(f"{cluster_emoticons[topic]} {topic}"):
            selected_cluster = dfs[topic]

# Display the selected cluster if it's not None
if selected_cluster is not None:
    st.subheader(f"Cluster: **{selected_cluster}**")
    books = selected_cluster

    # Pagination
    page_number = st.session_state.get('page_number', 0)
    if st.button("Previous") and page_number > 0:
        page_number -= 1
    if st.button("Next") and page_number < len(books) - 1:
        page_number += 1
    st.session_state['page_number'] = page_number

    # Display book information
    book = books.iloc[page_number]

    st.markdown(
        f"""
        <main>
            <div class="navbar bg-base-100 rounded-box shadow-lg mb-4 md:mb-6 max-w-[40rem] mx-auto">
                <div class="navbar-start w-1/4">
                    <button class="btn btn-square btn-ghost" aria-label="Go to homepage">
                        <div class="relative w-full aspect-square m-1">
                            <span style="box-sizing:border-box;display:block;overflow:hidden;width:initial;height:initial;background:none;opacity:1;border:0;margin:0;padding:0;position:absolute;top:0;left:0;bottom:0;right:0">
                                <img alt="Book Preview" src="{book['complete_link']}" decoding="async" data-nimg="fill" style="position: absolute; inset: 0px; box-sizing: border-box; padding: 0px; border: none; margin: auto; display: block; width: 0px; height: 0px; min-width: 100%; max-width: 100%; min-height: 100%; max-height: 100%;" sizes="100vw" srcset="{book['complete_link']}">
                            </span>
                        </div>
                    </button>
                </div>
                <div class="navbar-center w-1/2 justify-center">
                    <div class="nunito text-center tracking-tight">{book['title']}</div>
                </div>
                <div class="navbar-end w-1/4">
                    <button class="btn btn-primary btn-square md:btn-block nunito">🥰 Edit Mood</button>
                </div>
            </div>
        </main>
        """,
        unsafe_allow_html=True
    )
