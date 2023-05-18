#django imports
from django.shortcuts import render
from django.http import JsonResponse

#external imports
import requests

#local imports
from banking_api.settings import env

# Create your views here.
def get_weather_data(location):
    api_key = env('weather_api_key')
    url = f'https://api.weatherapi.com/v1/current.json?key={api_key}&q={location}'

    response = requests.get(url)

    if response.status_code == 200:
        weather_data = response.json()
        # Process and handle the weather data as per your requirements
        return weather_data
    else:
        # Handle the case when the request is unsuccessful
        print(f"Request failed with status code {response.status_code}")
        return None
    
def display_weather_info(request, location=None):
    weather_data = get_weather_data(location)

    if weather_data is not None:
        # Process the weather data further or display it
        return JsonResponse(weather_data)
    else:
        return JsonResponse('failed to retrieve weather data.')
