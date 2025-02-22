import cv2
import numpy as np
import os

# Loading the image
image = cv2.imread(r"C:\Users\Erica\Documents\Ery\4 SEMESTRE\undefined\WhatsApp Image 2024-12-12 at 18.41.42.jpeg")

# Defining the folders for the images
red_folder = r"C:\Users\Erica\Documents\Ery\4 SEMESTRE\algebra"
blue_folder = r"C:\Users\Erica\Documents\Ery\4 SEMESTRE\PAA"

# Checking if the image was loaded sucessfully
if image is None:
    print("Error: Image not found, try another path!")
else:
    print("Image loaded successfully!")
    
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
        folder = red_folder
    elif blue_pixels > red_pixels:
        folder = blue_folder
    else:
        folder = None

    #Displaying the results
    print("Number of red pixels: ", red_pixels)
    print("Number of blue pixels: ", blue_pixels)


    # Moving the image to the folder
    if folder:
        imwrite = cv2.imwrite(os.path.join(folder, "image.jpeg"), image)
        print("Image sucessfully moved to ", folder, "!")
    else:
        print("No color was predominant in the image!")



    # Displaying the image
    cv2.imshow("Image", image)
    cv2.waitKey(0) 
    cv2.destroyAllWindows()