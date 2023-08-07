import os
import numpy as np
import requests
import tensorflow as tf
import tempfile
from PIL import Image
from dotenv import load_dotenv

class FoodModel:
    def __init__(self):
        load_dotenv()  # take environment variables from .env.
        # Load the models
        self.food_model = self.load_model(os.getenv("FOOD_MODEL_URL"))
        self.classify_model = self.load_model(os.getenv("CLASSIFY_MODEL_URL"))
        self.class_labels_101 = ['apple_pie', 'baby_back_ribs', 'baklava', 'beef_carpaccio', 'beef_tartare', 'beet_salad', 'beignets', 'bibimbap', 'bread_pudding', 'breakfast_burrito', 'bruschetta', 'caesar_salad', 'cannoli', 'caprese_salad', 'carrot_cake', 'ceviche', 'cheese_plate', 'cheesecake', 'chicken_curry', 'chicken_quesadilla', 'chicken_wings', 'chocolate_cake', 'chocolate_mousse', 'churros', 'clam_chowder', 'club_sandwich', 'crab_cakes', 'creme_brulee', 'croque_madame', 'cup_cakes', 'deviled_eggs', 'donuts', 'dumplings', 'edamame', 'eggs_benedict', 'escargots', 'falafel', 'filet_mignon', 'fish_and_chips', 'foie_gras', 'french_fries', 'french_onion_soup', 'french_toast', 'fried_calamari', 'fried_rice', 'frozen_yogurt', 'garlic_bread', 'gnocchi', 'greek_salad', 'grilled_cheese_sandwich', 'grilled_salmon', 'guacamole', 'gyoza', 'hamburger', 'hot_and_sour_soup', 'hot_dog', 'huevos_rancheros', 'hummus', 'ice_cream', 'lasagna', 'lobster_bisque', 'lobster_roll_sandwich', 'macaroni_and_cheese', 'macarons', 'miso_soup', 'mussels', 'nachos', 'omelette', 'onion_rings', 'oysters', 'pad_thai', 'paella', 'pancakes', 'panna_cotta', 'peking_duck', 'pho', 'pizza', 'pork_chop', 'poutine', 'prime_rib', 'pulled_pork_sandwich', 'ramen', 'ravioli', 'red_velvet_cake', 'risotto', 'samosa', 'sashimi', 'scallops', 'seaweed_salad', 'shrimp_and_grits', 'spaghetti_bolognese', 'spaghetti_carbonara', 'spring_rolls', 'steak', 'strawberry_shortcake', 'sushi', 'tacos', 'takoyaki', 'tiramisu', 'tuna_tartare', 'waffles']



    def load_model(self, blob_url):
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

    def predict(self, model, image_array):
        # Use the model to make a prediction
        prediction = model.predict(np.array([image_array]))  # Wrap the image array in another array because model.predict expects a batch of images
        return prediction

    def preprocess_image(self, img, size):
        # Resize the image to desired size
        img = img.resize(size)
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

    def is_food(self, img):
        # Preprocess image
        image_array = self.preprocess_image(img, (224, 224))
        # Make a prediction
        prediction = self.predict(self.food_model, image_array)
        # Return whether or not the prediction is food
        return prediction[0][0] < 0.5

    def classify_food(self, img):
        # Preprocess image
        image_array = self.preprocess_image(img, (299, 299))
        # Make a prediction
        prediction = self.predict(self.classify_model, image_array)
        # Return whether or not the prediction is food
     
    
        return self.class_labels_101[np.argmax(prediction)], np.max(prediction)

