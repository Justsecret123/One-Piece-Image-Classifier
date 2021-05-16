# -*- coding: utf-8 -*-
"""
Created on Tue Jan  5 17:36:18 2021

@author: Ibrah
"""

import tensorflow as tf
import numpy as np
import matplotlib.pyplot as plt
import PIL

from tensorflow import keras 
from keras.preprocessing import image



#Load our trained model
path = "h5_model/Object_Detector_Model_KerasTuner_10epochs.h5"
model = keras.models.load_model(path)

#Load the image from disk
image_path = "Test images/Luffy.jpg"

#Image preprocessing
im = image.load_img(image_path,target_size=(180,180))
inputs = image.img_to_array(im)
inputs = tf.expand_dims(inputs,axis=0)
class_names = ['Luffy','Zoro','Sanji']

#Model prediction
prediction = model.predict(inputs)

#Sigmoid will return the probability of the image belonging to each class.
#Rather than a probability distribution, it is a set of probabilities.
#Each label has its own probability, which do not depend on another label's probability.
#Since we can have more than one character in the image, a sigmoid fits better than softmax which is a probability distribution. 
#In our case, { P(X=Luffy) = score[0]
#               P(X=Sanji) = score[2]
#               P(X=Unknown) = score[3]
#               P(x=Zoro) = score[4]
#             } 
score = tf.nn.sigmoid(prediction[0])

print("Image: ", image_path)

for i in range (len(score)):
    print("\nProbability of being " + class_names[i] + \
              ": ", 100*score[i].numpy() , "%")

    #print(predictions)
    
    object_score = np.max(score)
    object_class = class_names[np.argmax(score)]
        #np.argmax(score) returns the index with the highest score 
        #np.max(score) returns the highest probability of our input belonging to one of our classes
    
    
    print("This image most likely belongs to " +str(object_class)+ \
          " category with a " + str(object_score) + " score. \n\n"
    )
    
    
i = PIL.Image.open(image_path)
i.show()