import requests
from datetime import datetime

APP_ID = '843bc668'
API_KEY  = '615a86c1adc838fb16c9605fa5bcc148'

headers = {
    'x-app-id' : APP_ID,
    'x-app-key' : API_KEY
}

exercise = input("Tell me what excercises you did: ")

params = {
     "query": exercise
}

exercise_endpoint = 'https://trackapi.nutritionix.com/v2/natural/exercise'

response = requests.post(exercise_endpoint, headers=headers, json=params)
result = response.json()

for exercise_result in result["exercises"]:
    exercise = exercise_result['name'].title()
    duration = exercise_result['duration_min']
    calories = exercise_result['nf_calories']

today = datetime.now()
date = today.date()
time = f'{today.time().hour}:{today.time().minute}'


sheety_endpoint = 'https://api.sheety.co/938cf0496091dff68ea11077fd14c274/copyOfMyWorkouts/workouts'

sheety_input = {
    "workout" : {
        "date" : str(date),
        "time" : str(time),
        "exercise" : exercise.title(),
        "duration" : duration,
        "calories" : calories
    }
}

sheety_header = {
    'Authorization': 'Bearer YAHHOOyippieWAHHAA'
}

sheety_response = requests.post(sheety_endpoint, json=sheety_input, headers=sheety_header)
print(sheety_response.text)