import os
from roboflow import Roboflow

# Public Roboflow workspace for Autonomous Driving Dataset
try:
    print("Downloading dataset...")
    rf = Roboflow(api_key="PUBLIC_VSCODE_KEY")
    project = rf.workspace("roboflow-100").project("self-driving-car")
    dataset = project.version(1).download("yolov8")
    print("Dataset successfully downloaded!")
except Exception as e:
    print(f"Error downloading dataset: {e}")