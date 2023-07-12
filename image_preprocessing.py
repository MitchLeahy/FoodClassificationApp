from PIL import Image
import numpy as np

def preprocess_image(image):
    image_size = (224, 224)
    image = image.resize(image_size)  # Resize the image
    image = np.array(image)           # Convert the image to a numpy array
    image = image / 255.0             # Normalize the pixel values
    return image