import cv2
import gradio as gr
import numpy as np
import os
from PIL import Image
from try_on_diffusion_client import TryOnDiffusionClient   # <‑ the file you just pulled

# --- 1.  Initialise the API client -----------------------------------------
API_URL = "https://try-on-diffusion.p.rapidapi.com"   # RapidAPI endpoint
API_KEY = os.getenv("RAPIDAPI_KEY")                  # put your key in an env var
client  = TryOnDiffusionClient(base_url=API_URL, api_key=API_KEY)

# --- 2.  The Gradio callback ------------------------------------------------

def try_on(user_img, outfit_img, height, chest, waist, sleeve):
    # 1️⃣  Force 3‑channel RGB and uint8 dtype
    user_rgb   = user_img.convert("RGB")
    outfit_rgb = outfit_img.convert("RGB")

    avatar_bgr   = cv2.cvtColor(np.array(user_rgb,   dtype=np.uint8), cv2.COLOR_RGB2BGR)
    clothing_bgr = cv2.cvtColor(np.array(outfit_rgb, dtype=np.uint8), cv2.COLOR_RGB2BGR)

    # 2️⃣  Call the API (unchanged)
    resp = client.try_on_file(
        clothing_image = clothing_bgr,
        avatar_image   = avatar_bgr,
        seed           = -1
    )

    if resp.status_code != 200 or resp.image is None:
        return None, f"API error {resp.status_code}: {resp.error_details}"

    result_rgb = cv2.cvtColor(resp.image, cv2.COLOR_BGR2RGB)

    # 3️⃣  Simple fit message
    fit_msg = "✅ Fit looks OK"
    if chest < 80:
        fit_msg = "⚠️ Chest measurement suggests a tight fit."

    return Image.fromarray(result_rgb), fit_msg


# --- 3. Create the Gradio Interface ------------------------------------------
demo = gr.Interface(
    fn=try_on,
    inputs=[
        gr.Image(type="pil", label="Upload your image"),
        gr.Image(type="pil", label="Upload outfit image"),
        gr.Number(label="Height (cm)"),
        gr.Number(label="Chest (cm)"),
        gr.Number(label="Waist (cm)"),
        gr.Number(label="Sleeve length (cm)")
    ],
    outputs=[
        gr.Image(type="pil", label="Try-On Result"),
        gr.Text(label="Fit Advice")
    ],
    title="👕 Virtual Try-On",
    description="Upload your image and an outfit to see how it might look on you!"
)

# --- 4. Launch the app -------------------------------------------------------
if __name__ == "__main__":
    print("Launching Virtual Try-On App...")
    demo.launch()

