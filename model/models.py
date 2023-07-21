from _models import load_model, predict
from image_preprocessing import preprocess_image
import tensorflow as tf

# from PIL import Image
# import numpy as np

# def preprocess_image(uploaded_file):
#     # Open the image file
#     img = Image.open(uploaded_file)
    
#     # Resize the image to 224x224 pixels (this size is commonly used by image processing CNNs)
#     img = img.resize((224, 224))
    
#     # Convert the image to a numpy array
#     img_array = np.array(img)

#     # If the image is grayscale, convert it to RGB
#     if len(img_array.shape) == 2:
#         img_array = np.repeat(img_array[:, :, np.newaxis], 3, axis=2)
    
#     # If the image has an alpha channel, remove it
#     if img_array.shape[2] == 4:
#         img_array = img_array[:, :, :3]

#     # Normalize the image array (this helps CNNs perform better)
#     img_array = img_array / 255.0

#     return img_array
# def load_model(model_path):
#     # Load the model from the h5 file
#     model = tf.keras.models.load_model(model_path)
#     return model

# def predict(model, image):
#     # Use the model to make a prediction
#     prediction = model.predict(image)
#     return prediction

def is_food(image_path):
    # Load the model
    model = load_model("ViT_Food_5k.h5")
    # Load the image
    image = preprocess_image(image_path)
    # Make a prediction
    prediction = predict(model, image)
    # Return whether or not the prediction is food
    return prediction[0][0]
