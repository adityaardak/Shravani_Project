import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import datetime

MOOD_OPTIONS = ["😀 Happy", "😐 Neutral", "😢 Sad", "😠 Angry", "😞 Stressed"]

def main():
    st.title("📊 Mood Tracker")
    
    mood = st.selectbox("How are you feeling today?", MOOD_OPTIONS)
    
    if st.button("Log Mood"):
        with open("mood_logs.csv", "a") as file:
            file.write(f"{datetime.date.today()},{mood}\n")
        st.success("Mood logged successfully!")
    
    st.subheader("Mood Trends")
    try:
        df = pd.read_csv("mood_logs.csv", names=["Date", "Mood"])
        df["Date"] = pd.to_datetime(df["Date"])
        mood_counts = df["Mood"].value_counts()
        
        fig, ax = plt.subplots()
        ax.bar(mood_counts.index, mood_counts.values, color="skyblue")
        st.pyplot(fig)
    except:
        st.warning("No mood data available yet.")
