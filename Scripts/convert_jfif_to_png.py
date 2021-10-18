# -*- coding: utf-8 -*-
"""
Created on Fri Oct 15 10:10:17 2021

@author: Ibrah
"""

from glob import glob
import cv2 
import os

def main(input_dir):
    
    ## Get the file list
    files = glob(input_dir+"*.jfif")
    print(f"Files count: {len(files)}")
    
    ## Loop through the files list
    for file in files: 
        file_name = os.path.basename(file)
        print(f"Image: {file_name}")
        image = cv2.imread(file)
        cv2.imwrite(input_dir+"/"+file_name[0:-5]+".png",image) # Save the converted image
        os.remove(file)
        
    

if __name__ == "__main__":
    input_dir = "../Data/Usopp/" 
    main(input_dir)