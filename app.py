import streamlit as st
from PIL import Image
from food_api import get_nutrition_info, get_recipe
import json
from model.image_preprocessing import preprocess_image
from model._models import load_model, predict
# from model.models import is_food

#import here



# Read the list from the JSON file
with open('responses.json', 'r') as f:
    response_dict = json.load(f)


st.title("Food Classifier")

uploaded_file = st.file_uploader("Choose an image...", type="jpeg")

if uploaded_file is not None:
    image = Image.open(uploaded_file)
    st.image(image, caption='Uploaded Image.', use_column_width=True)

    st.write(preprocess_image(uploaded_file))

    st.write(load_model("model/ViT_Food_5k.h5"))

    # st.write("The class label you entered is:", is_food(uploaded_file))

    class_label = st.text_input("Enter the class label for this image")
    

    if st.button("Enter"):

    # Display nutrition info and recipe

        st.write(response_dict[class_label])
