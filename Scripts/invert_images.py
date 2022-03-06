# -*- coding: utf-8 -*-
"""
Created on Thu Oct  7 02:39:19 2021

@author: Ibrah
"""

import os
from glob import glob
import cv2 

# Constants
INPUT_DIR = "your_input_dir"
OUTPUT_DIR = "your_output_dir"

def main():
    """Main : loop through a folder then proceeds to invert all its images"""
    
    # Get the file list
    files = glob(INPUT_DIR + "/*")
    print(f"Files count: {len(files)}")
    
    # Loop through the files list
    for file in files: 
        # Get the basename (filename)
        file_name = os.path.basename(file)
        print(f"Image: {file_name}")
        
        # Read the file and invert the image
        image = cv2.imread(file)
        image_inverted = cv2.bitwise_not(image) 
        
        # Save the results
        cv2.imwrite(OUTPUT_DIR + file_name + "_inverted.png", image_inverted) 
        
    

if __name__ == "__main__":
    
    main()
    