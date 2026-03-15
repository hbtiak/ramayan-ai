import requests
from PIL import Image
from io import BytesIO
import random
import streamlit as st
import time

API_URL = "https://router.huggingface.co/hf-inference/models/stabilityai/stable-diffusion-2"

headers = {
    "Authorization": f"Bearer {st.secrets['HF_TOKEN']}"
}

def generate_ai_image(scene, style, exaggeration):

    prompt = f"""
    Epic mythological illustration of {scene},
    {style} style,
    exaggeration level {exaggeration},
    cinematic lighting,
    highly detailed artwork
    """

    for _ in range(5):

        response = requests.post(
            API_URL,
            headers=headers,
            json={"inputs": prompt},
            timeout=60
        )

        if response.status_code == 200:
            return Image.open(BytesIO(response.content))

        if "loading" in response.text.lower():
            st.warning("Model loading on server... retrying")
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
        "Heroic": ["gold","deep red","royal blue"],
        "Divine": ["white","gold","light blue"],
        "Battle": ["black","crimson","dark purple"],
        "Sunset": ["orange","pink","violet"]
    }

    return palettes.get(mood, [])
