import streamlit as st
from PIL import Image
import json
import pandas as pd
from model_stuff.model import FoodModel

# Initialize the FoodModel
food_model = FoodModel()

# Read the list from the JSON file
with open('recipe.json', 'r') as f:
    recipe_dict = json.load(f)


st.title("SnackSniffer")

uploaded_file = st.file_uploader("Insert a picture of your plate, we'll do the rest.", type="jpeg")

if uploaded_file is not None:
    image = Image.open(uploaded_file)
    st.image(image, caption='Uploaded Image.', use_column_width=True)

    if food_model.is_food(image):

        #classifys image
        class_label = food_model.classify_food(image)
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

        st.markdown(f"# [{class_label.replace('_',' ').title()}]({food['url']})")

        st.subheader("Ingredients:")
        # Display the DataFrame as a table in Streamlit
        st.dataframe(recipe_df.reset_index().drop(columns='index'))
        st.subheader(f"This recipe makes {food['yield']} serving sizes of {int(float(food['totalWeight'])/float(food['yield']))} grams  with an estimate of {int(float(food['calories'])/float(food['yield']))} calories per serving.") 

    else:
        st.title("Thas's not food silly goose!")
        st.image("sillier goose.jfif")
