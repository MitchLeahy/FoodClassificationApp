import streamlit as st
from PIL import Image
from food_api import get_nutrition_info, get_recipe
import json


#import here



# Read the list from the JSON file
with open('responses.json', 'r') as f:
    response_dict = json.load(f)


st.title("Food Classifier")

uploaded_file = st.file_uploader("Choose an image...", type="jpeg")

if uploaded_file is not None:
    image = Image.open(uploaded_file)
    st.image(image, caption='Uploaded Image.', use_column_width=True)

    class_label = st.text_input("Enter the class label for this image")

    if st.button("Enter"):
        # nutrition_info = get_nutrition_info(class_label)

        # picks the first search result and extracts the nutrients object specifically the 'KCAL' value
        # calories = [x['value'] for x in nutrition_info['foods'][0]['foodNutrients'] if x['unitName'] == 'KCAL'][0]
        # calories = nutrition_info


        # st.write(f"{class_label} has {calories} calories per serving size")
        # recipe = get_recipe(class_label)

    # Display nutrition info and recipe

        st.write(response_dict[class_label])
