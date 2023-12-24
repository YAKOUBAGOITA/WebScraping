import cv2

# Load an image from file
image_path = r'C:\Users\YAKOUBA GOITA\Desktop\ProductPal\ProductPal\__init__.py'  # Replace with the actual path to your image file
image = cv2.imread(image_path)

# Check if the image was successfully loaded
if image is not None:
    # Display the original image
    cv2.imshow('Original Image', image)
    
    # Wait for a key press and close the window
    cv2.waitKey(0)
    cv2.destroyAllWindows()
else:
    print(f"Error: Unable to load the image from {image_path}")
