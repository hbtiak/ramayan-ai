from diffusers import StableDiffusionPipeline
import torch
import random

device = "cuda" if torch.cuda.is_available() else "cpu"

pipe = StableDiffusionPipeline.from_pretrained(
    "runwayml/stable-diffusion-v1-5"
)

pipe = pipe.to(device)

def generate_ai_image(scene, style, exaggeration):

    prompt = f"""
    Epic mythological illustration of {scene},
    {style} style,
    exaggerated character design level {exaggeration},
    cinematic lighting,
    detailed artwork
    """

    image = pipe(prompt).images[0]

    return image


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

    return palettes.get(mood,[])
