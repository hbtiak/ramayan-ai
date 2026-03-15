import requests
from PIL import Image, ImageFilter
from io import BytesIO
import random
import streamlit as st
import numpy as np
import time

API_URL = "https://router.huggingface.co/hf-inference/models/stabilityai/stable-diffusion-xl-base-1.0"

headers = {
    "Authorization": f"Bearer {st.secrets['HF_TOKEN']}"
}


def preprocess_sketch(image):

    # convert to grayscale
    gray = image.convert("L")

    # detect edges
    edges = gray.filter(ImageFilter.FIND_EDGES)

    # convert back to RGB
    return edges.convert("RGB")


def generate_ai_image(scene, style, exaggeration, artist_image=None):

    prompt = f"""
    Epic mythological illustration of {scene}.
    Art style: {style}.
    Character exaggeration level {exaggeration}.
    Dramatic lighting.
    Highly detailed artwork.
    """

    files = None

    if artist_image is not None:

        sketch = preprocess_sketch(artist_image)

        buffer = BytesIO()
        sketch.save(buffer, format="PNG")
        buffer.seek(0)

        files = {"image": buffer}

    for _ in range(5):

        response = requests.post(
            API_URL,
            headers=headers,
            json={"inputs": prompt} if files is None else None,
            files=files,
            timeout=60
        )

        if response.status_code == 200:
            return Image.open(BytesIO(response.content))

        if "loading" in response.text.lower():
            st.warning("Model loading... retrying")
            time.sleep(8)
            continue

        st.error(response.text)
        return None

    st.error("Model took too long to start")
    return None


def suggest_layout(scene):

    layouts = [
        "Hero centered composition",
        "Low angle dramatic perspective",
        "Diagonal action layout",
        "Triangular battle composition"
    ]

    return random.choice(layouts)


def suggest_colors(mood):

    palettes = {
        "Heroic": ["gold", "deep red", "royal blue"],
        "Divine": ["white", "gold", "light blue"],
        "Battle": ["black", "crimson", "dark purple"],
        "Sunset": ["orange", "pink", "violet"]
    }

    return palettes.get(mood, [])
