import requests
import os
from dotenv import load_dotenv

load_dotenv()
API_KEY = os.getenv('ROBOFLOW_API')

project_id = "dogs-and-cats-lost-and-found"
model_version = 1
confidence = 0.75
iou_thresh = 0.5
api_key = API_KEY
task = "object_detection"

dog_response = requests.get("https://dog.ceo/api/breeds/image/random")
dog_data = dog_response.json()
image_url = dog_data.get("message")

if image_url:
    infer_payload = {
        "model_id": f"{project_id}/{model_version}",
        "image": {
            "type": "url",
            "value": image_url,
        },
        "confidence": confidence,
        "iou_threshold": iou_thresh,
        "api_key": api_key,
    }

    res = requests.post(
        f"http://35.229.122.140:9001/infer/{task}",
        json=infer_payload,
    )

    predictions = res.json()
    print(predictions)
else:
    print("Failed to fetch the dog image URL from the Dog API.")
