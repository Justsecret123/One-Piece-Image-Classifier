# -*- coding: utf-8 -*-
"""
Created on Fri Apr  8 18:23:49 2022

@author: Ibrah
"""

import argparse
import time
import io
import tensorflow as tf 
import requests
from PIL import Image
import cv2
import numpy as np

# Define classes
CLASSES = ['Ace', 'Akainu', 'Brook', 'Chopper', 'Crocodile', 'Franky', 
           'Jinbei', 'Kurohige', 'Law', 'Luffy', 'Mihawk', 
           'Nami', 'Robin', 'Sanji', 'Shanks','Usopp', 'Zoro']

# Input shape
INPUT_SHAPE = (224,224)

def load_model():
    """
    Load the model and its parameters

    Returns
    -------
    interpreter : TFLite interpreter for inferences
    input_details : model input details for inferences
    output_details : model output details for decoding the output

    """
    
    print("\nLoading the model...\n-----------------------")
    
    # Initialize the timer
    timer = time.time()
    
    # Load the interpreter (model)
    interpreter = tf.lite.Interpreter(model_path=MODEL)
    
    # Get the input and output details
    input_details = interpreter.get_input_details()
    output_details = interpreter.get_output_details()

    # Calculate and display the elapsed time
    timer = round(time.time() - timer, 2)
    print(f"Model loaded in: {timer}s\n")
    print(f"\nInput details : {input_details}")

    return interpreter, input_details, output_details
    

def get_image(): 
    """
    Returns
    -------
    image : 3-dimensional array
        Image which the inference wil be runned on.

    """
    print("Loading the image...\n-----------------------")
    
    # Initialize the timer
    timer = time.time()
    
    
    if MODE=="image": 
        # Loading the image
        image = tf.keras.utils.load_img(path=IMAGE_SOURCE, target_size=INPUT_SHAPE)
        # Converting the image to an array
        image = tf.keras.preprocessing.image.img_to_array(image)
    else: 
        # Download the image
        print("\nDownloading and converting the image...")
        dl_request = requests.get(IMAGE_SOURCE, stream=True)
        dl_request.raise_for_status()
        # Open the image
        image = Image.open(io.BytesIO(dl_request.content))
        # Convert to array
        image = tf.keras.preprocessing.image.img_to_array(image)
        # Remove the 4th channel if exists (convert from RGBA to RGB )
        image = cv2.cvtColor(image, cv2.COLOR_BGRA2BGR)
        # Resize to the input shape
        image = tf.image.resize(image, INPUT_SHAPE)
        print("\nDone!\n")
    
    
    # Calculate and display the elapsed time
    timer = round(time.time() - timer, 2)
    print(f"Image loaded in: {timer}s\n")
    print(f"Image shape: {image.shape}\n")
    
    return image

def inference(image, interpreter, input_details, output_details):
    """
    Parameters
    ----------
    image : array
        DESCRIPTION.
    interpreter : TF Lite interpreter
    input_details : Interpreter input details
    output_details : Interpreter output details

    Returns
    -------
    results : (1,15) array 
        Probability of the input belonging to each class.

    """
    
    print("Running inference...\n-----------------------")
    
    # Initialize the timer
    timer = time.time()
    
    
    # Create the input tensor
    input_tensor = tf.expand_dims(image,axis=0)
    
    # Setup the interpreter
    interpreter.allocate_tensors()
    interpreter.set_tensor(input_details[0]["index"], input_tensor)
    
    # Run inference
    interpreter.invoke()
    
    # Get the results 
    results = interpreter.get_tensor(output_details[0]["index"])
    
    # Calculate and display the elapsed time
    timer = round(time.time() - timer, 2)
    print(f"Inference time : {timer}s\n")
    
    return results
    
    
    

def main(): 
    """
    Main algorithm

    """
    
    # Load the model and its parameters
    interpreter, input_details, output_details = load_model()
    
    # Load the image as an input array
    image = get_image()
    
    # Run inference
    results = inference(image, interpreter, input_details, output_details)
    
    # Results intepretation
    predicted_class = CLASSES[np.argmax(results)]
    predicted_score = np.max(results)
    
    # Display the results
    print(f"\n[Image class : {predicted_class}, Probability: {predicted_score}]\n\n")


def create_parser(): 
    """
    Creates the argparser
    """
    
    # Initialize the parser
    parser = argparse.ArgumentParser(description="Runs inferences on an image")
    
    # Arguments
    
    # Model path
    parser.add_argument("-model", help="Model path")
    
    # Source : path to the image
    parser.add_argument("-source", help="Image path")
    
    # Mode : Image or URL
    parser.add_argument("-mode", default="image", help="Inference mode")
    
    return parser
    

if __name__ == "__main__": 
    
    # Generate the parser
    parser = create_parser()
    # Parse the command line args
    args = parser.parse_args()
    # Get the values as a dict(key,value)
    variables = vars(args)
    
    # Setup globals
    MODEL = variables["model"]
    IMAGE_SOURCE = variables["source"]
    MODE = variables["mode"]
    
    # Run the main algorithm
    main()
    