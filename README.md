## ImageClassifyHub

🖼️  ImageClassifyHub is a simple, easy-to-use web application for image classification. It allows you to upload images and get classification results using a pre-trained deep learning model. You can seamlessly connect your own image classification models to the app and run predictions in real-time.
Features

Image Upload: Upload images from your local machine.
Model Integration: Connect any pre-trained PyTorch model for image classification.
Real-time Classification: Get classification results and raw model outputs instantly after uploading the image.
Image Display: The uploaded image is displayed alongside the classification result.
Customizable: Modify the app to fit any image size or preprocessing steps as per your model's needs.



🛠️ Prerequisites

Python 3.6+
PyTorch
Flask
Torchvision
Pillow (for image handling)



📦 Installation

Clone the repository:


    git clone https://github.com/diana1800/ImageClassifyHub.git
    cd ImageClassifyHub


Install the required Python packages

Open your browser and go to: http://127.0.0.1:5000

Upload an image and get the classification result.



⚙️ Customization

Model Architecture: To use your own model modify models.py to define any custom architecture.

Model data: Place your trained model checkpoint (BestModel.pt) in the root directory.

Image Preprocessing: The image transformations can be customized to match the input format required by your model.

Deployment: This app is currently a development server (Flask)



💡 Contributing

Feel free to contribute to this project by submitting issues or pull requests!


![image](https://github.com/user-attachments/assets/3c7a9934-c054-4391-b087-1debac351b64)

