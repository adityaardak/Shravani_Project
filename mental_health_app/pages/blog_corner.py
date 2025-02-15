import streamlit as st
import sqlite3

def create_table():
    conn = sqlite3.connect("blog.db")
    cursor = conn.cursor()
    cursor.execute("CREATE TABLE IF NOT EXISTS posts (id INTEGER PRIMARY KEY, content TEXT, upvotes INTEGER)")
    conn.commit()
    conn.close()

def add_post(content):
    conn = sqlite3.connect("blog.db")
    cursor = conn.cursor()
    cursor.execute("INSERT INTO posts (content, upvotes) VALUES (?, ?)", (content, 0))
    conn.commit()
    conn.close()

def get_posts():
    conn = sqlite3.connect("blog.db")
    cursor = conn.cursor()
    cursor.execute("SELECT id, content, upvotes FROM posts ORDER BY upvotes DESC")
    posts = cursor.fetchall()
    conn.close()
    return posts

def upvote_post(post_id):
    conn = sqlite3.connect("blog.db")
    cursor = conn.cursor()
    cursor.execute("UPDATE posts SET upvotes = upvotes + 1 WHERE id = ?", (post_id,))
    conn.commit()
    conn.close()

def main():
    st.title("📝 Blog Corner")
    
    create_table()
    
    new_post = st.text_area("Share your thoughts anonymously:")
    if st.button("Post"):
        add_post(new_post)
        st.success("Post added successfully!")
    
    st.subheader("Community Posts")
    posts = get_posts()
    for post in posts:
        st.write(f"**{post[1]}**")
        st.button(f"👍 Upvote ({post[2]})", key=post[0], on_click=upvote_post, args=(post[0],))

