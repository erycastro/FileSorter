import cv2
import numpy as np

# Loading the image
image = cv2.imread(r"C:\Users\Erica\Documents\Ery\4 SEMESTRE\algebra\WhatsApp Image 2024-12-12 at 18.41.42.jpeg")

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

    # Displaying the image
    cv2.imshow("Image", image)
    cv2.waitKey(0) 
    cv2.destroyAllWindows()