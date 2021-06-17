# One-Piece-Image-Classifier

A quick image classifier trained with manually selected One Piece images. 

## Training 

The model was trained using Keras Tuner for finding the best training hyperparameters (learning rate and number of units in the flatten layer). No pre-trained model has been used. The training session has been runned on Google Colab with a GPU execution type. 

## Model summary

![Model_summary](Screenshots/Model%20summary.png)
> **The number of units within the Dense Layer has been obtained thanks to Keras fine tuning. Out of all the previously used method, this one has generated the best valdiation accuracy: 88.04%.**

## How to use 

### 1-First option: Google Colab

#### Step 1:  Run all the cells, then upload the files on which you want to make an inference by clicking on the upload button 
![Upload](Screenshots/Upload.PNG)

#### Step 2: Slide to the prediction results. You will get two messages displayed as shown in the following screenshots: 
![Probabilities](Screenshots/Probabilities.PNG)
> **Represents the probability of the character belonging to each class. These probabilities are mutually non-exclusive, since there can be more than one character within an image**

![Results](Screenshots/Results.PNG)


### 2-Second option: Through the test script

#### Navigate to the "image path" variable, and replace it with whatever file you want to perform the prediction/inference onto.
![Image_path](Screenshots/Image%20path.PNG). 

> **The resutls will be diplayed in a terminal, as shown in the "Probabilities" screenshot above. 

## Prerequisites

- Python 3.x or higher 
- IDE: Jupyter Lab/Google Colab
- Libraries: Pathlib, Zipfile, os
- Frameworks: Tensorflow 2.0 or higher, Keras
