from diffusers import StableDiffusionPipeline
from transformers import CLIPTextModel, CLIPTokenizer
import torch

def generate_image(prompt):
    # Ensure you have a GPU available (model is large and requires a GPU to run efficiently)
    device = "cuda" if torch.cuda.is_available() else "cpu"

    # Load the Stable Diffusion pipeline
    model_id = "CompVis/stable-diffusion-v1-4"  # or another model version
    pipe = StableDiffusionPipeline.from_pretrained(model_id, use_auth_token=True).to(device)

    # Generate an image from the text prompt
    image = pipe(prompt)["sample"][0]

    # Save the image
    image.save("generated_image.png")

# Example usage
generate_image("A futuristic city skyline at sunset")
