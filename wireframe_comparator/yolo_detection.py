import cv2
import torch
import numpy as np
from ultralytics import YOLO  # ✅ Use Ultralytics YOLO API

class YoloDetector:
    def __init__(self, model_path="yolo_model/yolov8x.pt", confidence_threshold=0.5):
        # ✅ Load YOLO model directly using Ultralytics
        self.model = YOLO(model_path)
        self.confidence_threshold = confidence_threshold

    def detect_objects(self, image_path):
        # ✅ Read the image
        image = cv2.imread(image_path)
        if image is None:
            raise FileNotFoundError(f"Image not found: {image_path}")

        # ✅ Run inference
        results = self.model(image)  # YOLO automatically handles preprocessing

        # ✅ Extract detections
        elements = []
        for result in results:
            for box in result.boxes:
                # ✅ Extract bounding box coordinates
                x_min, y_min, x_max, y_max = box.xyxy[0].tolist()

                # ✅ Extract confidence and class ID separately
                conf = box.conf[0].item() if box.conf is not None else 1.0
                class_id = int(box.cls[0].item()) if box.cls is not None else -1

                # ✅ Apply confidence threshold
                if conf >= self.confidence_threshold:
                    elements.append({
                        "x_min": int(x_min),
                        "y_min": int(y_min),
                        "x_max": int(x_max),
                        "y_max": int(y_max),
                        "confidence": float(conf),
                        "label": class_id
                    })

        return elements
