import requests
import os
from dotenv import load_dotenv

load_dotenv()

# 1
def random_joke() -> str:
    API_URL = "https://api.chucknorris.io/jokes/random/"
    
    outcome = ""
    
    try:
        outcome = requests.get(API_URL).json()["value"]
    except Exception as error:
        outcome = error
    
    return print(f"A random Chuck Norris joke: {outcome}")

#   random_joke()

# 2
API_KEY = os.getenv('OPEN_WEATHER_API_KEY')

def get_coordinates(city: str):
    API_URL = f"http://api.openweathermap.org/geo/1.0/direct?q={city}&appid={API_KEY}"
    
    try:
        response = requests.get(API_URL).json()[0]
        return {"latitude": response["lat"], "longitude": response["lon"]}
    except Exception as error:
        return print(error)
    
def city_weather() -> str:
    city = input("Input a city: ")
    units = input("Which units you want to display temperature in (F / C / K): ")

    coordinates = get_coordinates(city)
    API_URL = f"https://api.openweathermap.org/data/2.5/weather?lat={coordinates["latitude"]}&lon={coordinates["longitude"]}{f"&units={"metric" if units == "C" else "imperial"}" if units in ["C", "F"] else ""}&appid={API_KEY}"
    
    try:
        request = requests.get(API_URL).json()
        
        if request["cod"] == 200:
        
            weather_data = request["main"]
            temperature = weather_data["temp"]
            
            return print(f"Temperature in {city}: {temperature} {units}")
        else:
            return print(request["message"])
    except Exception as error:
        return print(error)
    
#   city_weather()