import streamlit as st
import sqlite3

def create_chat_table():
    conn = sqlite3.connect("community_chat.db")
    cursor = conn.cursor()
    cursor.execute("CREATE TABLE IF NOT EXISTS chat (message TEXT)")
    conn.commit()
    conn.close()

def add_message(message):
    conn = sqlite3.connect("community_chat.db")
    cursor = conn.cursor()
    cursor.execute("INSERT INTO chat (message) VALUES (?)", (message,))
    conn.commit()
    conn.close()

def get_messages():
    conn = sqlite3.connect("community_chat.db")
    cursor = conn.cursor()
    cursor.execute("SELECT message FROM chat")
    messages = cursor.fetchall()
    conn.close()
    return messages

def main():
    st.title("💬 Community Sessions")

    create_chat_table()

    new_message = st.text_input("Enter your message:")
    if st.button("Send"):
        add_message(new_message)
        st.success("Message sent!")

    st.subheader("Live Chat")
    messages = get_messages()
    for message in messages:
        st.write(f"🗨 {message[0]}")
