## ImageClassifyHub

ImageClassifyHub is a simple, easy-to-use web application for image classification. It allows you to upload images and get classification results using a pre-trained deep learning model. You can seamlessly connect your own image classification models to the app and run predictions in real-time.
Features

Image Upload: Upload images from your local machine.
Model Integration: Connect any pre-trained PyTorch model for image classification.
Real-time Classification: Get classification results and raw model outputs instantly after uploading the image.
Image Display: The uploaded image is displayed alongside the classification result.
Customizable: Modify the app to fit any image size or preprocessing steps as per your model's needs.

Prerequisites

Python 3.6+
PyTorch
Flask
Torchvision
Pillow (for image handling)

Installation

Clone the repository:


  git clone https://github.com/your-username/ImageClassifyHub.git
  cd ImageClassifyHub

Install the required Python packages

Add your PyTorch model in the models.py file.

Place your trained model checkpoint (BestModel.pt) in the root directory.



Open your browser and go to: http://127.0.0.1:5000

Upload an image and get the classification result along with the raw prediction score.

Model Integration

To use your own model, modify the models.py file to define your custom architecture. Make sure your model is saved as BestModel.pt and adjust the following code sections to match your model:

python

model = YourCustomModel()  
dCheckpoint = torch.load('BestModel.pt')
model.load_state_dict(dCheckpoint['Model'])
model.eval()

Example

Upload an image (e.g., a cat or a dog), and the app will classify it as either "Positive" or "Negative" based on the model's output. The app will also display the raw prediction score from the model.
Customization

Model Architecture: You can modify models.py to define any custom architecture.
Image Preprocessing: The image transformations can be customized to match the input format required by your model.
Deployment: This app is currently a development server (Flask). For production, consider deploying with WSGI servers like Gunicorn or using a cloud platform.

Contributing

Feel free to contribute to this project by submitting issues or pull requests!

Fork the repo.
Create your feature branch: git checkout -b feature/new-feature.
Commit your changes: git commit -m 'Add new feature'.
Push to the branch: git push origin feature/new-feature.
Submit a pull request.


![image](https://github.com/user-attachments/assets/3c7a9934-c054-4391-b087-1debac351b64)

