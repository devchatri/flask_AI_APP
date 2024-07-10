import replicate
import os
import requests

# Remplacez par votre jeton d'API Replicate
os.environ["REPLICATE_API_TOKEN"] = "r8_YuR3rKZrkqQCeb51S1qSnFEOrsA6TCe3Bch5m"

input = {
    "width": 768,
    "height": 768,
    "prompt": "An astronaut riding a rainbow unicorn, cinematic, dramatic",
    "refine": "expert_ensemble_refiner",
    "apply_watermark": False,
    "num_inference_steps": 25
}

output = replicate.run(
    "stability-ai/sdxl:7762fd07cf82c948538e41f63f77d685e02b063e37e496e96eefd46c929f9bdc",
    input=input
)

image_url = output[0]
print(image_url)

# Télécharger et enregistrer l'image localement
response = requests.get(image_url)
if response.status_code == 200:
    with open("output_image.png", "wb") as f:
        f.write(response.content)
    print("Image téléchargée et enregistrée sous 'output_image.png'.")
else:
    print("Erreur lors du téléchargement de l'image.")
