import os
from ultralytics import YOLO

def main():
    print("--- Starting Training & Prediction with Built-in Dataset ---")
    
    # 1. Pre-trained YOLOv8 Nano model load
    model = YOLO("yolov8n.pt")

    # 2. Train using YOLO's built-in lightweight COCO8 dataset (Auto downloads)
    print("Starting Model Training...")
    results = model.train(
        data="coco8.yaml",   # Built-in dataset
        epochs=5,            # Fast training
        imgsz=640,
        batch=4,
        workers=0
    )
    print("Training Complete!")

    # 3. Predict on a sample image (Vehicles & Persons)
    print("Running detection...")
    sample_img = "https://ultralytics.com/images/bus.jpg"
    predict_results = model.predict(source=sample_img, save=True, conf=0.25)
    
    print("\nSUCCESS! Detection result saved inside: runs/detect/predict/")

if __name__ == "__main__":
    main()