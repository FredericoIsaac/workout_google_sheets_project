import requests
import os
from datetime import datetime


API_ID = os.environ["API_ID"]
API_KEY = os.environ["API_KEY"]
URL_EXERCISE = os.environ["URL_EXERCISE"]


query = input("Tell me which exercises you did: ")

exercise_params = {
     "query": query,
     "gender": "male",
     "weight_kg": 62.5,
     "height_cm": 170.00,
     "age": 28
}

headers = {
     "x-app-id": API_ID,
     "x-app-key": API_KEY,
}

exercise_response = requests.post(url=URL_EXERCISE, headers=headers, json=exercise_params)
exercise_data = exercise_response.json()

SHEETY_URL = os.environ["SHEETY_URL"]


type_exercise = exercise_data["exercises"][0]["name"]
time_exercising = exercise_data["exercises"][0]["duration_min"]
calories_spent = exercise_data["exercises"][0]["nf_calories"]

today = datetime.now()
date = today.strftime("%d/%m/%Y")
time = today.strftime("%X")

TOKEN = os.environ["TOKEN"]

auth_sheety = {
     "Authorization": f"Bearer {TOKEN}"
}


new_row = {
     "workout": {
          "date": date,
          "time": time,
          "exercise": type_exercise,
          "duration": time_exercising,
          "calories": calories_spent,
     }
}

sheety_post = requests.post(url=SHEETY_URL, json=new_row, headers=auth_sheety)
print(sheety_post.text)
