import streamlit as st
from PIL import Image
from food_api import get_nutrition_info, get_recipe
import json
#import your model here
# e.g. from my_model import my_classifier



st.title("Food Classifier")

uploaded_file = st.file_uploader("Choose an image...", type="jpeg")

if uploaded_file is not None:
    image = Image.open(uploaded_file)
    st.image(image, caption='Uploaded Image.', use_column_width=True)

    class_label = st.text_input("Enter the class label for this image")

    if st.button("Enter"):
        nutrition_info = get_nutrition_info(class_label)

        calories = [x['value'] for x in nutrition_info['foods'][0]['foodNutrients'] if x['unitName'] == 'KCAL'][0]
        # calories = nutrition_info


        st.write(f"This food has {calories} calories per serving size")
    # recipe = get_recipe(class_label)

    # Display nutrition info and recipe

    # st.write("Recipe:", recipe)
