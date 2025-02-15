import streamlit as st

MUSIC_RECOMMENDATIONS = {
    "😀 Happy": "https://www.youtube.com/watch?v=ZbZSe6N_BXs",
    "😐 Neutral": "https://www.youtube.com/watch?v=JGwWNGJdvx8",
    "😢 Sad": "https://www.youtube.com/watch?v=09R8_2nJtjg",
    "😠 Angry": "https://www.youtube.com/watch?v=YQHsXMglC9A",
    "😞 Stressed": "https://www.youtube.com/watch?v=VJ2rlci9PE0"
}

def main():
    st.title("🎵 Music Therapy")
    
    mood = st.selectbox("Select your current mood:", list(MUSIC_RECOMMENDATIONS.keys()))
    
    st.subheader("Recommended Music for You 🎶")
    st.video(MUSIC_RECOMMENDATIONS[mood])
