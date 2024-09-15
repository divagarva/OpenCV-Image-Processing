import cv2
import os

# Load an image from the images directory
image_path = os.path.join("images", "sample_image.jpg")
image = cv2.imread(image_path)

if image is None:
    print(f"Error: Could not find the image at {image_path}")
    exit()

# Convert the image to grayscale
gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# Resize the image to 300x300 pixels
resized_image = cv2.resize(image, (300, 300))

# Apply Canny edge detection
edges = cv2.Canny(image, 100, 200)

# Display the original, grayscale, resized, and edge-detected images
cv2.imshow("Original Image", image)
cv2.imshow("Grayscale Image", gray_image)
cv2.imshow("Resized Image", resized_image)
cv2.imshow("Edge Detection", edges)

# Wait until any key is pressed to close the image windows
cv2.waitKey(0)
cv2.destroyAllWindows()
