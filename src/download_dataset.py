from roboflow import Roboflow
import os
from dotenv import load_dotenv

load_dotenv()
API_KEY = os.getenv('ROBOFLOW_API')

rf = Roboflow(api_key=API_KEY)
project = rf.workspace("smonyl").project("dogs-and-cats-lost-and-found")
dataset = project.version(1).download("yolov8")
