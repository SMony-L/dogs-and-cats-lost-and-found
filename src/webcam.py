import cv2
import inference
import supervision as sv
import os 
from dotenv import load_dotenv

load_dotenv()
API_KEY = os.getenv('ROBOFLOW_API')

annotator = sv.BoxAnnotator()

def on_prediction(predictions, image):
    labels = [p["class"] for p in predictions["predictions"]]
    detections = sv.Detections.from_roboflow(predictions)
    cv2.imshow(
        "Prediction",
        annotator.annotate(
            scene=image,
            detections=detections,
            labels=labels
        )
    ),
    cv2.waitKey(1)

inference.Stream(
    api_key=API_KEY,
    source="webcam", # or rtsp stream or camera id
    model="dogs-and-cats-lost-and-found/1", # from Universe
    output_channel_order="BGR",
    use_main_thread=True, # for opencv display
    on_prediction=on_prediction,
)