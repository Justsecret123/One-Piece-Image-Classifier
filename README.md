# One-Piece-Image-Classifier ![Language_support](https://img.shields.io/pypi/pyversions/Tensorflow) ![Last_commit](https://img.shields.io/github/last-commit/JustSecret123/Human-pose-estimation) ![Workflow](https://img.shields.io/github/workflow/status/JustSecret123/Human-pose-estimation/Pylint/main) ![Tensorflow_version](https://img.shields.io/badge/Tensorflow%20version-2.6.2-orange)

A quick image classifier trained with manually selected One Piece images. 97.80% validation accuracy.

> **Deployed on my personal Docker Hub repository: [Click here](https://hub.docker.com/repository/docker/ibrahimserouis/my-tensorflow-models)

> **Kaggle Notebook link:  [Kaggle notebook](https://www.kaggle.com/ibrahimserouis99/one-piece-image-classifier-notebook)

> **Tensorflow Lite model : [op_classifier_V14.tflite](https://drive.google.com/file/d/1-xTYqv10IQmV0FS3ftYH6LeTbE86dlkT/view?usp=sharing)

<a href="https://www.linkedin.com/in/ibrahim-serouis-b05378181/">
  <img src="https://img.shields.io/badge/LinkedIn-Ibrahim%20Serouis-blue?link=http://left&link=http://right)"/>
</a>


## Training 

A fine-tuned mobilenet has been used. The training session has been runned on Google Colab with a GPU execution type. 

## Notebook 

> Notebook link : [Click here](one-piece-image-classifier-notebook.ipynb)

## Model description

- A data augmentation layer which creates "modified" images of the training set
- A MobileNet layer which detects the features
- A Global average pooling layer which converts the feature vectors into a 1280 element vector
- 1*3 Dense layers followed by a dropout layer to avoid overfitting
- An activation layer (sigmoid) which represents the final output: Probability of input(X) belonging to each class
- Output classes (probabilities) : ['Ace', 'Akainu', 'Brook', 'Chopper', 'Crocodile', 'Franky', 'Jinbei', 'Law', 'Luffy', 'Nami', 'Robin', 'Sanji', 'Shanks', 'Usopp', 'Zoro']

## Architecture

![Model architecture](Screenshots/Model_summary_new.PNG)
> **Best valdiation accuracy: 97.80%.**

## Results (Amazon SageMaker endpoint)

![Results](Screenshots/One%20Piece%20image%20classifier.gif)

# Useful scripts 
- [JFIFF to PNG converter](/Scripts/convert_jfif_to_png.py)
- [Image inverter](Scripts/invert_images.py)

## How to use 

### 1-First option: Using the [command line runner](Scripts/op_classifier.py)

#### Args 

![Args](Screenshots/command_line_args.PNG)

> **The image source can be a file path or a URL**

#### Results 
![Results](Screenshots/command_line_results.PNG)

### 2-Second option: Using the Tensorflow Serving image deployed [here](https://hub.docker.com/repository/docker/ibrahimserouis/my-tensorflow-models) (**TAG: OP_serving**)

Pull the Docker image with the OP_serving tag, then run inferences using the 8501 port. 

> A test script example is available [here](/Scripts/Prediction_OP_Model_Test.py)


## Prerequisites

- Python 3.7 or higher 
- IDE: Jupyter Lab/Kaggle Notebooks/Google Colab 
- Frameworks: Tensorflow 2.6 or higher and its dependencies
- Libraries : OpenCV, PIL, NumPy
