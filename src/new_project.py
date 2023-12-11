from roboflow import Roboflow
import os
from dotenv import load_dotenv

load_dotenv()
API_KEY = os.getenv('ROBOFLOW_API')

rf = Roboflow(api_key=API_KEY)

# create a project if you have not create one
# rf.create_project(
#     project_name="project name",
#     project_type="project-type",
#     license="project-license" # "private" for private projects
# )

workspace = rf.workspace("smonyl")
project = workspace.project("dogs-and-cats-lost-and-found")
version = project.version("v1")

# upload a dataset
project.upload_dataset(
    dataset_path="./data/",
    num_workers=10,
    dataset_format="yolov8", # supports yolov8, yolov5, and Pascal VOC
    project_license="MIT",
    project_type="object-detection"
)
