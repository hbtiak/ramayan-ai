import streamlit as st
from PIL import Image
from utils import generate_ai_image, suggest_layout, suggest_colors

st.set_page_config(
    page_title="Epic AI Storytelling Studio",
    layout="wide"
)

st.title("🎨 Human-Centered AI for Epic Storytelling")
st.subheader("Artist + AI Co-Creation Tool")

st.markdown(
"""
Upload your caricature or sketch, describe a scene, and let AI help turn it into an epic illustration.
The artist remains in control while AI suggests layouts, colors, and enhanced artwork.
"""
)

# --- Sidebar controls ---

st.sidebar.header("Creative Controls")

scene = st.sidebar.text_area(
    "Scene Description",
    "Rama aiming his bow at Ravana during the final battle"
)

style = st.sidebar.selectbox(
    "Art Style",
    [
        "Comic book",
        "Caricature",
        "Indian miniature painting",
        "Digital painting",
        "Mythological epic",
        "Watercolor illustration"
    ]
)

exaggeration = st.sidebar.slider(
    "Character Exaggeration",
    1,
    10,
    5
)

mood = st.sidebar.selectbox(
    "Color Mood",
    ["Heroic", "Divine", "Battle", "Sunset"]
)

# --- Main layout ---

col1, col2 = st.columns(2)

# Artist upload
with col1:

    st.header("Artist Input")

    uploaded_file = st.file_uploader(
        "Upload your caricature / sketch",
        type=["png", "jpg", "jpeg"]
    )

    if uploaded_file:

        artist_image = Image.open(uploaded_file)

        st.image(
            artist_image,
            caption="Uploaded Artist Sketch",
            width="stretch"
        )

    else:
        artist_image = None


# AI suggestions
with col2:

    st.header("AI Suggestions")

    if st.button("Suggest Layout"):

        layout = suggest_layout(scene)

        st.success(f"Suggested Layout: {layout}")

    if st.button("Suggest Colors"):

        palette = suggest_colors(mood)

        st.write("Recommended Color Palette:")
        for color in palette:
            st.write(f"• {color}")


st.divider()

# --- Generate AI Illustration ---

st.header("Generate Illustration")

if st.button("Generate Illustration"):

    with st.spinner("Generating AI illustration..."):

        img = generate_ai_image(
            scene,
            style,
            exaggeration,
            artist_image
        )

        if img is not None:

            st.subheader("AI Illustration")

            st.image(
                img,
                width="stretch"
            )

        else:

            st.warning("Image generation failed. Try again.")
