
import random
from PIL import Image, ImageDraw

# Lightweight placeholder generator so the demo runs without heavy AI models
def generate_ai_image(scene, style, exaggeration):
    width, height = 768, 512
    img = Image.new("RGB", (width, height), "white")
    draw = ImageDraw.Draw(img)

    text = f"Scene: {scene}\nStyle: {style}\nExaggeration: {exaggeration}%"
    draw.text((40, 200), text, fill="black")

    return img

def suggest_layout(scene):
    layouts = [
        "Hero centered composition with dramatic sky",
        "Low angle perspective emphasizing scale",
        "Diagonal action composition for motion",
        "Triangular composition for visual tension"
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
