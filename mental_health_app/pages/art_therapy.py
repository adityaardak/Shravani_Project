import streamlit as st
from streamlit_drawable_canvas import st_canvas

def main():
    st.title("🎨 Art Therapy")

    st.write("Express yourself with digital drawing!")
    
    canvas = st_canvas(
        stroke_width=3,
        stroke_color="#000000",
        background_color="#FFFFFF",
        height=400,
        width=600,
        drawing_mode="freedraw",
        key="canvas",
    )

    if st.button("Save Drawing"):
        st.success("Your drawing has been saved! (Functionality pending)")
