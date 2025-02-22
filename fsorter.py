import cv2

# Loading the image
image = cv2.imread(r"C:\Users\Erica\Documents\Ery\4 SEMESTRE\algebra\WhatsApp Image 2024-12-12 at 18.41.42.jpeg")

# Displaying the image and waiting for a key to be pressed to close the image
cv2.imshow("Image", image)
cv2.waitKey(0) 
cv2.destroyAllWindows()