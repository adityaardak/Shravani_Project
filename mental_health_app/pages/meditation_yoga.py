import streamlit as st

YOGA_VIDEOS = {
    "Beginner Meditation": "https://www.youtube.com/watch?v=inpok4MKVLM",
    "Yoga for Relaxation": "https://www.youtube.com/watch?v=v7AYKMP6rOE",
}

def main():
    st.title("🧘 Meditation & Yoga")
    
    choice = st.selectbox("Choose a guided session:", list(YOGA_VIDEOS.keys()))
    
    st.video(YOGA_VIDEOS[choice])
