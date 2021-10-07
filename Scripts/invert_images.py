# -*- coding: utf-8 -*-
"""
Created on Thu Oct  7 02:39:19 2021

@author: Ibrah
"""


from glob import glob
import cv2 
import os



def main(input_dir, output_dir):
    
    ## Get the file list
    files = glob(input_dir+"/*")
    print(f"Files count: {len(files)}")
    
    ## Loop through the files list
    for file in files: 
        file_name = os.path.basename(file)
        print(f"Image: {file_name}")
        image = cv2.imread(file)
        image_inverted = cv2.bitwise_not(image) # Invert the image
        cv2.imwrite(output_dir+file_name+"_inverted.png",image_inverted) # Save the inverted image
        
    

if __name__ == "__main__":
    input_dir = "../Data/Nami" 
    output_dir = "../Data/Nami-inverted/"
    main(input_dir,output_dir)