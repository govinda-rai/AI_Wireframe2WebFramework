# Placeholder for segmentation.py
from keras_unet.models import custom_unet
from keras_unet.utils import plot_segm_history, plot_imgs
import cv2
import numpy as np

def unet_model(input_shape=(128, 128, 3), num_classes=5):
    return custom_unet(
        input_shape=input_shape,
        use_batch_norm=True,
        num_classes=num_classes,
        filters=64,
        dropout=0.3,
        output_activation='softmax'
    )

def segment_image(model, image):
    image_resized = cv2.resize(image, (128, 128))
    prediction = model.predict(np.expand_dims(image_resized, axis=0))
    return prediction
