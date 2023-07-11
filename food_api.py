import requests
import json
from dotenv import load_dotenv
import os

load_dotenv()  # take environment variables from .env.
food_api_key = os.getenv("FOOD_API_KEY")  # if not found, returns None
if not food_api_key:
    food_api_key = os.environ.get("FOOD_API_KEY")  # if not found, returns None

    
def get_nutrition_info(food_name):
    # This function would use an API or dataset to get nutrition info for the given food
    # e.g., using the Spoonacular API:
    
    url = f"https://api.nal.usda.gov/fdc/v1/foods/search?api_key={food_api_key}"
    headers = {
        "Content-Type": "application/json"
    }
    data = {
        "query": food_name,
        # "dataType": 'Survey (FNDDS)',
    }

    response = requests.post(url, headers=headers, data=json.dumps(data))

# print th
    # make sure the request was successful
    if response.status_code == 200:
        # parse the response as JSON
        # response_data = response.json()

        return response.json()
    else:
        return f"Failed to get data: {response.status_code} {response.text}"

# Define function to get recipe
def get_recipe(food_name):
    # This function would use an API or dataset to get a recipe for the given food
    # e.g., using the Spoonacular API:
    response = requests.get(f"https://api.spoonacular.com/recipes/complexSearch?query={food_name}&apiKey=YOUR_API_KEY")
    return response.json()
    pass