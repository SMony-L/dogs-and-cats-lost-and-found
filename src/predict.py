from roboflow import Roboflow
import os
from dotenv import load_dotenv

load_dotenv()
API_KEY = os.getenv('ROBOFLOW_API')

rf = Roboflow(api_key=API_KEY)
project = rf.workspace().project("dogs-and-cats-lost-and-found")
model = project.version(1).model

image_directory = "./data/prediction_images/"

prediction_results = []

# Iterate through each image in the directory
for filename in os.listdir(image_directory):
    if filename.endswith(".jpeg") or filename.endswith(".jpg"):
        image_path = os.path.join(image_directory, filename)
        
        # Predict on the current image
        prediction_result = model.predict(image_path, confidence=40, overlap=30).json()
        
        # Append the result to the list
        prediction_results.append(prediction_result)

for result in prediction_results:
    if len(result['predictions']) > 0:
        image_path = result['predictions'][0]['image_path']
        predicted_class = result['predictions'][0]['class']
        print(f"{image_path} is a {predicted_class}")
