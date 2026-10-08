import requests
import os 
from datetime import datetime
from dotenv import load_dotenv

load_dotenv()

API_KEY = os.getenv("WEATHERSTACK_API_KEY")
def get_weather(location):
    url = "http://api.weatherstack.com/current"


    params = {
        "access_key": API_KEY,
        "query": location
    }

    response = requests.get(url,params=params)
    data = response.json()

    if "error" in data:
            print("Weather error:", data["error"]["info"])
            return "Sorry sir, I couldn't find the weather for that location."

    temperature = data["current"]["temperature"]
    condition = data["current"]["weather_descriptions"][0]

    now = datetime.now()

    date = now.strftime("%d %B %Y")
    time = now.strftime("%I:%M %p")

    return (
        f"Today is {date}, and the current time is {time}. \n"
        f"The temperature in {location} is {temperature} degrees Celsius \n"
        f"with {condition}."
    )

if __name__ == "__main__":
    print(get_weather("Delhi"))