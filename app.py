import streamlit as st
from streamlit.report_thread import get_report_ctx
from streamlit.server.server import Server

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

# Function to retrieve the session state
def get_session_state():
    ctx = get_report_ctx()
    session = None
    session_infos = Server.get_current()._session_info_by_id.values()
    for session_info in session_infos:
        if session_info.session.id == ctx.session_id:
            session = session_info.session
            break
    return session

# Define the UI layout
def display_homepage():
    st.title("Dork's Data Digest")
    st.subheader("Discover top-rated books based for Data Science")
    for cluster in dfs.keys():
        if st.button(cluster):
            session_state = get_session_state()
            session_state.selected_cluster = cluster
            st.experimental_rerun()

# Display the selected cluster page
def display_cluster_page():
    session_state = get_session_state()
    selected_cluster = session_state.selected_cluster
    st.subheader(f"Cluster: {selected_cluster}")
    st.write(dfs[selected_cluster])

# Main function to switch between pages
def main():
    session_state = get_session_state()
    if hasattr(session_state, 'selected_cluster'):
        display_cluster_page()
    else:
        display_homepage()

# Run the app
if __name__ == "__main__":
    main()
