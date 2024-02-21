from dotenv import load_dotenv
import os
from transformers import pipeline

load_dotenv()

access_token = os.getenv("ACCESS_TOKEN", None)
default_model_name = os.getenv("DEFAULT_MODEL_NAME", "Falconsai/nsfw_image_detection")
default_score = os.getenv("DEFAULT_SCORE", 0.7)


def check_model(model_name):
    _model_name = model_name or default_model_name
    classifier = pipeline("image-classification", model=_model_name, token=access_token)
    classifier.save_pretrained(f"models/{_model_name}")

    return classifier