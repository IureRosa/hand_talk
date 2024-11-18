import torch
from transformers import AutoTokenizer
from diffusers import StableDiffusionPipeline
import base64
from io import BytesIO
from PIL import Image
import json

def load_pipeline():
    model_id = "gsdf/DreamShaper-v1.5"
    pipe = StableDiffusionPipeline.from_pretrained(model_id, torch_dtype=torch.float16)
    pipe.to("cuda")
    return pipe

def generate_image(data):
    try:
        person = data.get("person")
        instrument = data.get("instrument")
        environment = data.get("environment")
        style = data.get("style")

        prompt = f"A {person} playing a {instrument} in a {environment} in the style of {style}"

        pipe = load_pipeline()

        image = pipe(prompt).images[0]

        buffered = BytesIO()
        image.save(buffered, format="PNG")
        img_str = base64.b64encode(buffered.getvalue()).decode("utf-8")

        return img_str
    except Exception as e:
        raise Exception(f"Error generating image: {str(e)}")
