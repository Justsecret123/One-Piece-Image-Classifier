# -*- coding: utf-8 -*-
"""
Created on Thu Oct 14 09:09:59 2021

@author: Ibrah
"""

from glob import glob
import cv2 
import os



def main(input_dir):
    
    ## Get the file list
    files = glob(input_dir+"/*.jfif")
    print(f"Files count: {len(files)}")
    
    ## Loop through the files list
    for file in files: 
        file_name = os.path.basename(file)
        print(f"Image: {file_name}")
        image = cv2.imread(file)
        cv2.imwrite(input_dir+"/"+file_name+".png",image) # Save the converted image
        os.remove(input_dir+"/"+file_name) #Delete the .jfif image
        
    

if __name__ == "__main__":
    directories = {"Luffy","Nami","Franky","Sanji","Zoro","Brook"}
    for directory in directories: 
        input_dir = f"../Data/{directory}"
        main(input_dir)