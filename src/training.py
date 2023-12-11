from ultralytics import YOLO

# Adjust the path to your data.yaml file
data_path = './Dogs-and-Cats-Lost-and-Found-1/data.yaml'

# Load a pretrained YOLO model
model = YOLO('yolov8n.pt')

# Train the model
results = model.train(data=data_path, epochs=3)
