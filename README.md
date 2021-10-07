# One-Piece-Image-Classifier

A quick image classifier trained with manually selected One Piece images. 

## Training 

The model was trained using Keras Tuner for finding the best training hyperparameters (learning rate and number of units in the flatten layer). No pre-trained model has been used. The training session has been runned on Google Colab with a GPU execution type. 

## Model description

- 3 Convolutional layers followed by a batch normalization layer, then a MaxPooling layer followed by a batch normalization layer
- A flatten layer
- A dense layer which number of units will be decided by the hyper parameters
- An activation layer (sigmoid) which represents the final output: Probability of input(X) belonging to each class
> **Based on Sergey Ioffe and Christian Szegedy "Batch Normalization: Accelerating Deep Network Training by Reducing Internal Covariate Shift" research paper, there is no need to add a dropout layer since we've used a batch normalization layer.**
- Output classes (probabilities) : Luffy, Nami, Sanji, Zoro

## Architecture

![Model architecture](Screenshots/Architecture.png)
> **The number of units within the Dense Layer has been obtained thanks to Keras fine tuning. Out of all the previously used method, this one has generated the best valdiation accuracy: 86.74%.**

## How to use 

### 1-First option: Using the Tensorflow Serving image deployed ![here](https://hub.docker.com/repository/docker/ibrahimserouis/my-tensorflow-models) **TAG: OP_serving**

Pull the Docker imae with the OP_serving tag, then run inferences using the 8501 port. Tightly respect the model input architecture (batch_size, 180, 180, 3). 

### 2-Second option: Google Colab

#### Step 1:  Run all the cells, then upload the files on which you want to make an inference by clicking on the upload button 
![Upload](Screenshots/Upload.PNG)

#### Step 2: Slide to the prediction results. You will get two messages displayed as shown in the following screenshots: 
![Probabilities](Screenshots/Probabilities.PNG)
> **Represents the probability of the character belonging to each class. These probabilities are mutually non-exclusive, since there can be more than one character within an image**

![Results](Screenshots/Luffy%20Nami%20Results.PNG)

![Results](Screenshots/Zoro%20Sanji%20Results.PNG)


## Prerequisites

- Python 3.x or higher 
- IDE: Jupyter Lab/Google Colab
- Libraries: Pathlib, Zipfile, os
- Frameworks: Tensorflow 2.0 or higher, Keras
