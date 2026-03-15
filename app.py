
import streamlit as st
from PIL import Image
from utils import generate_ai_image, suggest_layout, suggest_colors

st.set_page_config(page_title="Epic AI Studio", layout="wide")

st.title("Epic AI Studio")
st.caption("Human-Centered AI for Mythological Storytelling Demo")

left, center, right = st.columns([1,2,1])

with left:
    st.header("Scene Controls")

    scene = st.text_area(
        "Describe Scene",
        "Hanuman flying toward Lanka carrying the mountain"
    )

    style = st.selectbox(
        "Art Style",
        ["Caricature", "Mythological Painting", "Comic Book", "Watercolor"]
    )

    exaggeration = st.slider(
        "Character Exaggeration",
        0, 100, 40
    )

    mood = st.selectbox(
        "Scene Mood",
        ["Heroic","Divine","Battle","Sunset"]
    )

    generate = st.button("Generate Illustration")

with center:
    st.header("Artist Canvas")

    uploaded = st.file_uploader(
        "Upload Sketch",
        type=["png","jpg","jpeg"]
    )

    if uploaded:
        sketch = Image.open(uploaded)
        st.image(sketch, use_column_width=True)
    else:
        st.info("Upload a rough sketch to guide the AI")

with right:
    st.header("AI Suggestions")

    if st.button("Suggest Layout"):
        st.success(suggest_layout(scene))

    if st.button("Suggest Colors"):
        colors = suggest_colors(mood)
        st.write(colors)

if generate:
    with st.spinner("AI creating illustration..."):
        img = generate_ai_image(scene, style, exaggeration)

        if img is not None:
            st.subheader("AI Illustration")
            st.image(img, use_column_width=True)
        else:
            st.warning("Image generation failed. Try again.")
