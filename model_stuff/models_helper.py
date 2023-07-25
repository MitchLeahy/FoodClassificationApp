import tensorflow as tf
import requests
import numpy as np
import tempfile

def load_model(blob_url):
    # Send HTTP GET request to the blob URL
    response = requests.get(blob_url)
    response.raise_for_status()  # Ensure we notice bad responses

    # Create a temporary file
    with tempfile.NamedTemporaryFile(delete=True) as tmp:
        # Write the response content to the temporary file
        tmp.write(response.content)
        tmp.flush()  # Ensure all data is written

        # Load the model from the temporary file
        model = tf.keras.models.load_model(tmp.name)

    return model


def predict(model, image_array):
    # Use the model to make a prediction
    prediction = model.predict(np.array([image_array]))  # Wrap the image array in another array because model.predict expects a batch of images
    return prediction
