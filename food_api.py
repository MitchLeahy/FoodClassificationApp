# import requests
# import json
# from dotenv import load_dotenv
# import os

# load_dotenv()  # take environment variables from .env.
# food_api_key = os.getenv("FOOD_API_KEY")  # if not found, returns None
# if not food_api_key:
#     food_api_key = os.environ.get("FOOD_API_KEY")  # if not found, returns None

    
# def get_nutrition_info(food_name):
#     # This function would use an API or dataset to get the search results for the given food
#     url = f"https://api.nal.usda.gov/fdc/v1/foods/search?api_key={food_api_key}"
#     headers = {
#         "Content-Type": "application/json"
#     }
#     data = {
#         "query": food_name,
   
#     }

#     response = requests.post(url, headers=headers, data=json.dumps(data))

#     # make sure the request was successful
#     if response.status_code == 200:

#         return response.json()
#     else:
#         return f"Failed to get data: {response.status_code} {response.text}"

# # function to get recipe
# def get_recipe(food_name):
#     # This function would use an API or dataset to get a recipe for the given food
 
#     response = requests.get(f"http://www.themealdb.com/api/json/v1/1/search.php?s={food_name}")
#     return response.json()
    