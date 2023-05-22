import cv2
import numpy as np

# Function to create a red color mask
def create_red_mask(image):
    # Convert the image to the HSV color space
    hsv = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)

    # Define the lower and upper bounds for red color
    lower_red = np.array([0, 50, 50])
    upper_red = np.array([10, 255, 255])
    upper_red2 = np.array([170, 255, 255])

    # Create a mask using the red color range
    mask1 = cv2.inRange(hsv, lower_red, upper_red)
    mask2 = cv2.inRange(hsv, lower_red, upper_red2)
    mask = cv2.bitwise_or(mask1, mask2)

    return mask

# Function to apply the red color mask on the image
def apply_red_mask(image, mask):
    
    foreground = cv2.bitwise_and(image, image, mask=mask)


    background = np.zeros_like(image)     # Create a black background

    return foreground, background

# Load the image
image = cv2.imread('test.png')

# Create the red color mask
red_mask = create_red_mask(image)

# Apply the red color mask on the image
foreground, background = apply_red_mask(image, red_mask)

# Show the original image, foreground (masked image), and black background

cv2.imshow('Foreground (Masked Image)', foreground)
cv2.imshow('Background', background)
cv2.waitKey(0)
cv2.destroyAllWindows()

#BETTER USE PHOTOSHOP :)
