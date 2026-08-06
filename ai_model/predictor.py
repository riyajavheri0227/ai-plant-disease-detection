import os
import json
import numpy as np
from PIL import Image
import onnxruntime as ort

# Folder containing this file
BASE_DIR = os.path.dirname(os.path.abspath(__file__))

# Load model
session = ort.InferenceSession(
    os.path.join(BASE_DIR, "model.onnx")
)

# Load class names
with open(os.path.join(BASE_DIR, "class_names.json"), "r") as f:
    class_names = json.load(f)


def predict_disease(image_path):
    # Open image
    image = Image.open(image_path).convert("RGB")

    # Resize to model size
    image = image.resize((224, 224))

    # Convert to numpy array
    image = np.array(image).astype(np.float32)

    # Normalize to 0-1
    image = image / 255.0

    # Change shape from (224,224,3) to (3,224,224)
    image = np.transpose(image, (2, 0, 1))

    # Add batch dimension
    image = np.expand_dims(image, axis=0)

    # Run model
    outputs = session.run(
        None,
        {"input": image}
    )

    # Get prediction scores
    scores = outputs[0][0]

    # Highest confidence index
    predicted_index = np.argmax(scores)

    # Confidence percentage
    exp_scores = np.exp(scores - np.max(scores))
    probabilities = exp_scores / np.sum(exp_scores)
    confidence = float(probabilities[predicted_index]) * 100

    # Return disease name and confidence
    return class_names[predicted_index], confidence