import cv2
import numpy as np


def create_color_mask(image, color_lower, color_upper):
    
    hsv = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)

    mask = cv2.inRange(hsv, color_lower, color_upper)

    return mask


def apply_color_mask(image, mask):
    
    inverse_mask = cv2.bitwise_not(mask)


    background = cv2.bitwise_and(image, image, mask=inverse_mask)

    return background


image = cv2.imread('test.jpg')

# Define the color range for masking (in HSV)
color_lower = np.array([0, 100, 100])  # Lower range of color (in HSV)
color_upper = np.array([10, 255, 255])  # Upper range of color (in HSV)


mask = create_color_mask(image, color_lower, color_upper)


masked_image = apply_color_mask(image, mask)

# Show the original image and the masked image
cv2.imshow('Masked Image', masked_image)
cv2.waitKey(0)
cv2.destroyAllWindows()
