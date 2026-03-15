import requests
from PIL import Image
from io import BytesIO
import random
import streamlit as st

API_URL = "https://api-inference.huggingface.co/models/stabilityai/stable-diffusion-2"

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

    try:
        response = requests.post(
            API_URL,
            headers=headers,
            json={"inputs": prompt},
            timeout=120
        )

        if response.status_code != 200:
            st.error("HuggingFace API Error")
            st.write(response.text)
            return None

        return Image.open(BytesIO(response.content))

    except Exception as e:
        st.error("Image generation failed")
        st.write(str(e))
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
