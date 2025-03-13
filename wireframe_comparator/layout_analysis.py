# Placeholder for layout_analysis.py
from yolo_detection import YoloDetector
from segmentation import unet_model, segment_image
import cv2

def analyze_layout(wireframe_path, screenshot_path):
    detector = YoloDetector()
    wireframe_elements = detector.detect_objects(wireframe_path)
    screenshot_elements = detector.detect_objects(screenshot_path)

    mismatches = []
    for i, wireframe_elem in enumerate(wireframe_elements):
        if i >= len(screenshot_elements):
            mismatches.append({"wireframe": wireframe_elem, "screenshot": None})
            continue
        screenshot_elem = screenshot_elements[i]
        if not elements_match(wireframe_elem, screenshot_elem):
            mismatches.append({"wireframe": wireframe_elem, "screenshot": screenshot_elem})

    return mismatches

def elements_match(wireframe_elem, screenshot_elem, tolerance=5):
    return (
        abs(wireframe_elem["x_min"] - screenshot_elem["x_min"]) <= tolerance and
        abs(wireframe_elem["y_min"] - screenshot_elem["y_min"]) <= tolerance and
        abs(wireframe_elem["width"] - screenshot_elem["width"]) <= tolerance and
        abs(wireframe_elem["height"] - screenshot_elem["height"]) <= tolerance
    )
