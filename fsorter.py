import cv2
import numpy as np
import os
import shutil

# Defining input folder
input_folder = r"C:\Users\Erica\Documents\Ery\sorterfolders\undefined"

# Defining the folders for the images
red_folder = r"C:\Users\Erica\Documents\Ery\sorterfolders\red"
blue_folder = r"C:\Users\Erica\Documents\Ery\sorterfolders\blue"

# Processing and moving the images
def process_images(input_folder, red_folder, blue_folder):
    # Verifying if the directories exist and creating them if they don't
    os.makedirs(red_folder, exist_ok=True)
    os.makedirs(blue_folder, exist_ok=True)
    
    # Iterating over the images in the input folder
    for image_name in os.listdir(input_folder):
        image_path = os.path.join(input_folder, image_name)

        # Verifying if the file is an image
        if image_name.lower().endswith(('.png', '.jpg', '.jpeg', '.tiff', '.bmp', '.gif')):
            # Loading the image
            image = cv2.imread(image_path)

            if image is None:
                print("Error loading image ", image_name, ". Moving to next image.")
                continue

            # Converting the image to HSV
            hsv = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)

            # Defining the range of red and blue color in HSV
            lower_red = np.array([0, 50, 50])
            upper_red = np.array([10, 255, 255])
            mask_red = cv2.inRange(hsv, lower_red, upper_red)

            lower_blue = np.array([110, 50, 50])
            upper_blue = np.array([130, 255, 255])
            mask_blue = cv2.inRange(hsv, lower_blue, upper_blue)

            # Counting the number of pixels in each color
            red_pixels = np.sum(mask_red > 0)
            blue_pixels = np.sum(mask_blue > 0)

            # Deciding which folder to save the image
            if red_pixels > blue_pixels:
                destination_folder = red_folder
                print(f"{image_name} classified as red")
            elif blue_pixels > red_pixels:
                destination_folder = blue_folder
                print(f"{image_name} classified as blue")
            else:
                print(f"No predominant color in image {image_name}. Moving to next image.")
                continue
            
            #Checking if the image already exists in the destination folder
            if os.path.exists(os.path.join(destination_folder, image_name)):
                print(f"{image_name} already exists in {destination_folder}!\n")
            else:
                # Defining the destination path
                destination_path = os.path.join(destination_folder, image_name)

            # Moving the image
            shutil.move(image_path, destination_path)
            print(f"{image_name} moved to {destination_folder}!\n")


process_images(input_folder, red_folder, blue_folder) 