def generate_ai_image(scene, style, exaggeration, artist_image=None):

    style_hint = ""

    if artist_image is not None:
        style_hint = "inspired by the uploaded artist sketch, bold outlines and caricature style"

    prompt = f"""
    Epic mythological illustration of {scene}.
    {style_hint}
    Art style: {style}.
    Character exaggeration level {exaggeration}.
    Dramatic cinematic lighting.
    Highly detailed epic artwork.
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
            st.warning("Model loading... retrying")
            time.sleep(8)
            continue

        st.error(response.text)
        return None

    st.error("Model took too long to start")
    return None
