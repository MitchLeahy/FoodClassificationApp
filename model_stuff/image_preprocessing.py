from PIL import Image
import numpy as np

def preprocess_image_is_food(img):
    # Resize the image to 224x224 pixels
    img = img.resize((224, 224))
    
    # Convert the image to a numpy array
    img_array = np.array(img)

    # If the image is grayscale, convert it to RGB
    if len(img_array.shape) == 2:
        img_array = np.repeat(img_array[:, :, np.newaxis], 3, axis=2)
    
    # If the image has an alpha channel, remove it
    if img_array.shape[2] == 4:
        img_array = img_array[:, :, :3]

    # Normalize the image array
    img_array = img_array / 255.0

    return img_array
def preprocess_image_classify_food(img):
    # Resize the image to 224x224 pixels
    img = img.resize((299, 299))
    
    # Convert the image to a numpy array
    img_array = np.array(img)

    # If the image is grayscale, convert it to RGB
    if len(img_array.shape) == 2:
        img_array = np.repeat(img_array[:, :, np.newaxis], 3, axis=2)
    
    # If the image has an alpha channel, remove it
    if img_array.shape[2] == 4:
        img_array = img_array[:, :, :3]

    # Normalize the image array
    img_array = img_array / 255.0

    return img_array