# -*- coding: utf-8 -*-
"""
Created on Fri Oct 15 10:10:17 2021

@author: Ibrah
"""

import os
from glob import glob
import cv2 

# Constant
INPUT_DIR = "your_input_directory" 

def main():
    """Main : loop through a folder then proceeds to convert JFIFF files to PNG files """
    
    # Get the file list
    files = glob(INPUT_DIR + "*.jfif")
    print(f"Files count: {len(files)}")
    
    # Loop through the files list
    for file in files: 
        # Get the basename (filename)
        file_name = os.path.basename(file)
        print(f"Image: {file_name}")
        image = cv2.imread(file)
        # Convert and save the image 
        cv2.imwrite(INPUT_DIR + "/"+ file_name[0:-5]+".png", image) 
        # Remove the old file
        os.remove(file)
    
if __name__ == "__main__":
    
    main()
    