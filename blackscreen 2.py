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

# Function to apply the red color mask on the image and replace the background
def replace_red_background(image, mask, background):
    # Use the red color mask to extract the foreground
    foreground = cv2.bitwise_and(image, image, mask=mask)

    # Invert the mask to extract the background
    inverse_mask = cv2.bitwise_not(mask)
    inverse_mask = cv2.cvtColor(inverse_mask, cv2.COLOR_GRAY2BGR)

    # Resize the background image to match the foreground image size
    background_resized = cv2.resize(background, (image.shape[1], image.shape[0]))

    # Apply the inverse mask on the background image
    background_removed = cv2.bitwise_and(background_resized, inverse_mask)

    
    result = cv2.add(foreground, background_removed)

    return result

# Load the image
image = cv2.imread('test.jpg')

# Create the red color mask
red_mask = create_red_mask(image)

# Load the background image
background = cv2.imread('bangkok.jpg')


result = replace_red_background(image, red_mask, background)

# Show the original image and the resulting image

cv2.imshow('Result', result)
cv2.waitKey(0)
cv2.destroyAllWindows()
