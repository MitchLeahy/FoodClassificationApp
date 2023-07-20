import tensorflow as tf


def load_model(model_path):
    try:
        # Load the model from the h5 file
        model = tf.keras.models.load_model(model_path)
        return model
    except Exception as e:
        print(f"Error: {e}")
        return None


def predict(model, image):
    # Use the model to make a prediction
    prediction = model.predict(image)
    return prediction