import requests
from PIL import Image
from io import BytesIO
import streamlit as st
import cv2
import numpy as np
import time

API_URL = "https://router.huggingface.co/hf-inference/models/stabilityai/stable-diffusion-xl-base-1.0"

headers = {
    "Authorization": f"Bearer {st.secrets['HF_TOKEN']}"
}


def preprocess_sketch(image):

    img = np.array(image)

    gray = cv2.cvtColor(img, cv2.COLOR_RGB2GRAY)

    edges = cv2.Canny(gray, 100, 200)

    edges = cv2.cvtColor(edges, cv2.COLOR_GRAY2RGB)

    return Image.fromarray(edges)


def generate_ai_image(scene, style, exaggeration, artist_image=None):

    prompt = f"""
    Epic Ramayan illustration of {scene}.
    Art style: {style}.
    Character exaggeration level {exaggeration}.
    Mythological epic artwork.
    Dramatic lighting.
    """

    if artist_image is not None:

        sketch = preprocess_sketch(artist_image)

        buffered = BytesIO()
        sketch.save(buffered, format="PNG")
        buffered.seek(0)

        files = {"image": buffered}

    else:
        files = None

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
