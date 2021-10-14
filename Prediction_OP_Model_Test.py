# -*- coding: utf-8 -*-
"""
Created on Mon Sep 13 02:29:52 2021

@author: Ibrah
"""

import io
import json
import cv2

import numpy as np
import requests

from tensorflow import expand_dims
from keras.preprocessing import image
from PIL import Image

# Define classes
classes = ["Brook","Franky","Luffy","Nami","Sanji", "Zoro"]

# Image URL Location
IMAGE_URL = 'https://static.wikia.nocookie.net/onepiece/images/4/4b/Sanji_Post_Ellipse_Portrait.png/revision/latest/scale-to-width-down/180?cb=20200803083919&path-prefix=fr'


# API endpoint
SERVER_URL = 'http://localhost:8501/v1/models/OP_model:predict'


def main():
    # Download the image
    dl_request = requests.get(IMAGE_URL, stream=True)
    dl_request.raise_for_status()

    # Compose a JOSN Predict request (send the image tensor).
    jpeg_rgb = Image.open(io.BytesIO(dl_request.content))
    inputs = image.img_to_array(jpeg_rgb)
    inputs = cv2.cvtColor(inputs, cv2.COLOR_BGRA2BGR)
    inputs = np.vstack([inputs])
    
    # Normalize and batchify the image
    inputs = expand_dims(inputs,axis=0)
    jpeg_rgb = inputs.numpy().tolist()
    predict_request = json.dumps({'instances': jpeg_rgb})
    
    # Send few requests to warm-up the model.
    for _ in range(3):
        response = requests.post(SERVER_URL, data=predict_request)
        response.raise_for_status()
        
    # Send few actual requests and report average latency.
    total_time = 0
    num_requests = 10
    for _ in range(num_requests):
        response = requests.post(SERVER_URL, data=predict_request)
        response.raise_for_status()
        total_time += response.elapsed.total_seconds()
        prediction = response.json()['predictions'][0]
    
    # Print the results
    print(f"Prediction class: { classes[np.argmax(prediction)] } \
          \n\nPrediction score: {np.max(prediction)} \ Average latency: { round((total_time * 1000) / num_requests,2)} ms")


if __name__ == '__main__':
  main()