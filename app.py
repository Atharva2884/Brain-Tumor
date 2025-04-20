from flask import Flask, render_template, request, redirect
from transformers import AutoImageProcessor, AutoModelForImageClassification
from PIL import Image
import torch
import numpy as np
import os

# Load Hugging Face model and processor
processor = AutoImageProcessor.from_pretrained("ShimaGh/Brain-Tumor-Detection")
model = AutoModelForImageClassification.from_pretrained("ShimaGh/Brain-Tumor-Detection")

# Class labels (update these based on the model's actual classes)
class_labels = ['glioma', 'meningioma', 'no_tumor', 'pituitary']  # Verify these with the model's actual classes

app = Flask(__name__)

def load_and_preprocess_image(img_path):
    """Load and preprocess an image for prediction using Hugging Face processor."""
    img = Image.open(img_path)
    inputs = processor(images=img, return_tensors="pt")
    return inputs

@app.route('/', methods=['GET', 'POST'])
def index():
    predicted_class_name = None
    confidence = None
    img_filename = None
    
    if request.method == 'POST':
        if 'file' not in request.files:
            return redirect(request.url)
        file = request.files['file']
        if file.filename == '':
            return redirect(request.url)

        # Save the uploaded file to a temporary location
        img_filename = file.filename
        img_path = os.path.join('static', img_filename)
        file.save(img_path)

        # Load and preprocess the image
        inputs = load_and_preprocess_image(img_path)

        # Make prediction
        with torch.no_grad():
            outputs = model(**inputs)
        
        # Get probabilities using softmax
        probabilities = torch.nn.functional.softmax(outputs.logits, dim=-1)
        top_prob, top_class = torch.topk(probabilities, 1)
        
        predicted_class_index = top_class.item()
        predicted_class_name = class_labels[predicted_class_index]
        confidence = round(top_prob.item() * 100, 2)  # Convert to percentage

    return render_template('index.html', 
                         tumor_type=predicted_class_name, 
                         confidence=confidence, 
                         filepath=img_filename)

if __name__ == '__main__':
    app.run(debug = True, host='0.0.0.0', port=5000)