import streamlit as st
import pandas as pd

def math_page():
    st.title("Mathematics Books")
# Load the dataset
    df = pd.read_csv("datasets/Mathematics.csv")
    
    # Get the theme background color
    background_color = st.get_option("theme.backgroundColor")
    
    st.markdown(
        f"""
        <style>
            .navbar {{
                background-color: {background_color};
                padding: 1rem;
                border-radius: 10px;
                box-shadow: 0px 2px 5px rgba(0, 0, 0, 0.1);
                margin-bottom: 2rem;
            }}
            .card {{
                border-radius: 10px;
                box-shadow: 0px 2px 5px rgba(0, 0, 0, 0.1);
                padding: 1rem;
                margin-bottom: 2rem;
            }}
            .video-responsive {{
                overflow: hidden;
                padding-bottom: 56.25%;
                position: relative;
                height: 0;
            }}
            .video-responsive iframe {{
                left: 0;
                top: 0;
                height: 100%;
                width: 100%;
                position: absolute;
            }}
            .button-group {{
                margin-top: 1rem;
                display: flex;
                justify-content: space-between;
                align-items: center; /* Align items vertically */
            }}
            .publisher, .pages, .price {{
                margin-top: 0.5rem;
                font-size: 14px;
                color: #555; /* Set color for text */
            }}
            .publisher {{
                font-weight: bold; /* Set font weight for publisher */
            }}
            .info {{
                display: flex;
                justify-content: space-between;
            }}
        </style>
        """,
        unsafe_allow_html=True
    )
    
    # Use session state to track the current index
    if 'index' not in st.session_state:
        st.session_state.index = 0
    
    if st.session_state.index < 0:
        st.session_state.index = 0
    elif st.session_state.index >= len(df):
        st.session_state.index = len(df) - 1
    
    row = df.iloc[st.session_state.index]
    
    st.markdown(
        f"""
        <div class="card">
            <div class="card-body">
                <h2 class="card-title tracking-tight cursor-pointer whitespace-nowrap overflow-auto noScroolBar nunito" data-tip="Click to copy title" currentitem="false">{row['title']}</h2>
                <div class="info">
                    <div class="publisher">Publisher: {row['publisher']}</div>
                </div>
                <div class="reviews"> Reviews on Amazon ⭐ <span class="font-semibold">{row['avg_reviews']}</span><span class="opacity-75">/5</span></div>
                <div class="info">
                    <div class="pages"><strong>Pages:</strong> {row['pages']}</div>
                    <div class="price"><strong>Price:</strong> ${row['price']}</div>
                </div>
                <div class="amazon-link">
                        <a href="{row['complete_link']}" target="_blank" class="btn nunito"><span class="mr-1">View on Amazon</span>🛒</a>
                </div>
            </div>
        </div>
        """,
        unsafe_allow_html=True
    )

    col1, col2, col3 = st.columns([1, 3, 1])
    if col1.button("⬅️ Previous"):
        st.session_state.index = max(st.session_state.index - 1, 0)
    with col3:
        if st.button("Next ➡️", key="next_button"):
            st.session_state.index = min(st.session_state.index + 1, len(df) - 1)

if __name__ == "__main__":
    math_page()
