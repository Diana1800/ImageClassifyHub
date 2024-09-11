import os
from flask import Flask, request, render_template_string, jsonify, send_from_directory
from PIL import Image
import torch
import torchvision.transforms as transforms
from models import ModifiedEfficientNet 
from werkzeug.utils import secure_filename


# Initialize your model
model = ModifiedEfficientNet()
# Load your trained model
dCheckpoint = torch.load('BestModel.pt')
model.load_state_dict(dCheckpoint['Model'])
model.eval()

# Define image transformations 
transform = transforms.Compose([
    transforms.Resize((224, 224)),  # Resize image to 224x224 (adjust as per your model)
    transforms.ToTensor(),
    transforms.Normalize([0.485, 0.456, 0.406], [0.229, 0.224, 0.225])  # Normalization based on ImageNet dataset
])

# Directory to save uploaded images
UPLOAD_FOLDER = 'uploads'

# Initialize Flask app
app = Flask(__name__)
app.secret_key = os.urandom(24)

app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
if not os.path.exists(UPLOAD_FOLDER):
    os.makedirs(UPLOAD_FOLDER)

# Route for rendering the main page
@app.route('/')
def index():
    return render_template_string(template)

# Route to handle image upload and classification
@app.route('/', methods=['POST'])
def classify_image():
    if 'image_file' not in request.files:
        return jsonify({'response': 'No image uploaded'}), 400
    
    image_file = request.files.get('image_file')
    if image_file.filename == '':
        print("Error: No selected file")
        return jsonify({'response': 'No selected file'}), 400

    
    filename = secure_filename(image_file.filename)
    image_path = os.path.join(app.config['UPLOAD_FOLDER'], filename)
    image_file.save(image_path)
    print(f"Image uploaded successfully: {image_path}")

    # Open the image file
    image = Image.open(image_path).convert('RGB')

    # Apply transformations
    input_tensor = transform(image).unsqueeze(0)  # Add batch dimension

    # Make the prediction
    with torch.no_grad():
        output = model(input_tensor)
    
    # Assuming your model outputs a single value for binary classification
    prediction = torch.sigmoid(output).item()
    print(f"Model prediction: {prediction}")

    # Convert prediction to positive/negative classification
    classification = "Positive" if prediction >= 0.5 else "Negative"

    # Return the classification result and image path
    return jsonify({'response': classification, 'image_path': f'/uploads/{filename}'})

@app.route('/uploads/<filename>')
def uploaded_file(filename):
    return send_from_directory(app.config['UPLOAD_FOLDER'], filename)

if __name__ == '__main__':
    app.run(port=5000)
