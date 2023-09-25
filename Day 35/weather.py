import requests

API_KEY = 'a420556f54fe8237f1af7f6d495cbc16'

lat = 35.898907
lon = 14.514553

req_url = f'https://api.openweathermap.org/data/2.5/onecall'
weather_params = {
    'lat' : lat,
    'lon' : lon,
    'appid': API_KEY
}

response = requests.get(req_url, params=weather_params)
response.raise_for_status()
data = response.json()

print(data)