import requests

def getWeather(city):
    response = requests.get("http://api.weatherstack.com/current?access_key=e2777bef4bee297e1c99800b853e4e53&query=" + city)

    if response.status_code != 200:
        print("Error fetching weather!")
        return None

    data = response.json()
    return {
        "temperature": data["current"]["temperature"],
        "weather_descriptions": data["current"]["weather_descriptions"],
        "wind_speed": data["current"]["wind_speed"],
        "humidity": data["current"]["humidity"]
    }

city = input("Enter a city: ")
weather = getWeather(city)

for k, x in weather.items():
    print(f"{k.title()}: {x}")


