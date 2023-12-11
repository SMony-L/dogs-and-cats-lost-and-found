
# Dogs and Cats Lost and Found Detection

## Project Overview

This project leverages machine learning and computer vision to identify lost dogs and cats. Using images sourced from APIs and processed via Roboflow, the project employs a YOLOv8 model (trained using Roboflow & Ultralytics) for object detection. The goal is to create a robust model that can accurately detect and differentiate between dogs and cats in various environments.

## Prerequisites
Before starting with the project, you will need to:

1. Sign up for Roboflow: A Roboflow account is required to manage datasets and models. Sign up at [Roboflow](https://roboflow.com/) and obtain your API key.

2. Create a dotenv file 

## Setup and Installation

1. **Clone the Repository**:
    ```
    git clone https://github.com/SMony-L/dogs-and-cats-lost-and-found.git
    cd dogs-cats-lost-found
    ```

2. **Install Required Libraries**:
    - Ensure Python is installed on your system.
    - Install necessary packages:
      ```
      pip install -r requirements.txt
      ```

## Usage

1. **Dataset Preparation**:
    - Run the `get_cats.sh` and `get_dogs.sh` scripts in `scripts/` to fetch images.
        - Note: For get_cats.sh you need to sign up in order to use the Cat API. Read more [here](https://thecatapi.com/)
    - Use `src/download_dataset.py` to download the dataset from Roboflow.
        ```
        python src/download_dataset.py
        ```

2. **Training the Model**:
    1. Train a Model in [Roboflow](https://docs.roboflow.com/train/train)
    2. Train locally with Ultralytics 
        - Navigate to `src/` and run `training.py` to train the model with Ultralytics YOLOv8.
        - Trained model weights will be saved in the `runs/` directory.
    ```
    python src/training.py
    ```
3. **Running Predictions**:
    - Use `src/predict.py` to make predictions on new images located in `data/prediction_images/`.
        - Note: this prediction is based on trained model from Roboflow
    ```
    python src/predict.py
    ```

4. **Google Colab Notebooks**:
    - Notebooks for training, prediction, and dataset downloading are available for use in Google Colab.
    - Upload `Dogs_and_Cats_Lost_and_Found.ipynb` to Google Colab
    - Open notebook with the GitHub Repository `https://github.com/SMony-L/dogs-and-cats-lost-and-found.git`
