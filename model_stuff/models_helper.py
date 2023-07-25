import tensorflow as tf

import numpy as np

def load_model(model_path):
    # try:
    # Load the model from the h5 file
    model = tf.keras.models.load_model(model_path)
    return model
    # except Exception as e:
    #     print(f"Error: {e}")
    #     return None


def predict(model, image_array):
    # Use the model to make a prediction
    prediction = model.predict(np.array([image_array]))  # Wrap the image array in another array because model.predict expects a batch of images
    return prediction
