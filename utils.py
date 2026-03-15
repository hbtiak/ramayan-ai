def generate_ai_image(scene, style, exaggeration):

    prompt = f"""
    Epic mythological illustration of {scene},
    {style} style,
    exaggeration level {exaggeration},
    cinematic lighting,
    highly detailed artwork
    """

    for _ in range(5):   # retry 5 times
        response = requests.post(
            API_URL,
            headers=headers,
            json={"inputs": prompt},
            timeout=60
        )

        if response.status_code == 200:
            return Image.open(BytesIO(response.content))

        # If model is loading
        if "loading" in response.text.lower():
            st.warning("Model is loading on server, retrying...")
            import time
            time.sleep(10)
            continue

        st.error(response.text)
        return None

    st.error("Model took too long to start. Try again.")
    return None
