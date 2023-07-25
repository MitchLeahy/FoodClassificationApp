import streamlit as st
from PIL import Image
import json
import pandas as pd
from model_stuff.image_preprocessing import preprocess_image_classify_food, preprocess_image_is_food
from model_stuff.models import is_food, classify_food



# Read the list from the JSON file
with open('recipe.json', 'r') as f:
    recipe_dict = json.load(f)


st.title("Food Classifier")

uploaded_file = st.file_uploader("Choose an image...", type="jpeg")

if uploaded_file is not None:
    image = Image.open(uploaded_file)
    st.image(image, caption='Uploaded Image.', use_column_width=True)
    # need two seperate images for the two models
    image1 = preprocess_image_is_food(image)
    image2 = preprocess_image_classify_food(image)

    if is_food(image1):

        #classifys image
        class_label = classify_food(image2)
        # gets food object from recipe.json
        food = recipe_dict[class_label]
        #isolates ingredients
        recipe = food['ingredients']

        # Convert the API response to a pandas DataFrame
        recipe_df = pd.DataFrame(recipe)
        # Only keep the necessary columns
        recipe_df = recipe_df[['food', 'quantity', 'measure']]
        #replace na with 'To taste'
        recipe_df = recipe_df.fillna('To taste')
        

        st.markdown(f"# [{class_label}]({food['url']})")

        st.subheader("Ingredients:")
        # Display the DataFrame as a table in Streamlit
        st.dataframe(recipe_df.reset_index().drop(columns='index'))
        st.subheader(f"This recipe makes {food['yield']} serving sizes of {int(float(food['totalWeight'])/float(food['yield']))} grams with an estimate of {int(float(food['calories'])/float(food['yield']))} calories per serving.") 
        st.write(food)
        



    else:
        st.write("This is not food!")


 
