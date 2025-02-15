import streamlit as st

# Set up navigation
st.sidebar.title("Mental Health App")
page = st.sidebar.radio("Go to", [
    "Blog Corner", "Mood Tracker", "Music Therapy",
    "Art Therapy", "Meditation & Yoga", "Community Sessions"
])

# Importing pages dynamically
if page == "Blog Corner":
    from pages import blog_corner
    blog_corner.main()
elif page == "Mood Tracker":
    from pages import mood_tracker
    mood_tracker.main()
elif page == "Music Therapy":
    from pages import music_therapy
    music_therapy.main()
elif page == "Art Therapy":
    from pages import art_therapy
    art_therapy.main()
elif page == "Meditation & Yoga":
    from pages import meditation_yoga
    meditation_yoga.main()
elif page == "Community Sessions":
    from pages import community_sessions
    community_sessions.main()
