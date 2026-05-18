# import requests

# def get_weather(city, api_key):
#     """
#     Fetch current weather data for a given city using OpenWeatherMap API.
#     """
#     base_url = "https://api.openweathermap.org/data/2.5/weather"
#     params = {
#         "q": city,
#         "appid": api_key,
#         "units": "metric"  # Celsius; use 'imperial' for Fahrenheit
#     }

#     try:
#         response = requests.get(base_url, params=params, timeout=5)
#         response.raise_for_status()  # Raise error for HTTP issues

#         data = response.json()

#         # Extract useful info
#         weather_desc = data["weather"][0]["description"].capitalize()
#         temp = data["main"]["temp"]
#         feels_like = data["main"]["feels_like"]
#         humidity = data["main"]["humidity"]

#         return {
#             "city": data["name"],
#             "temperature": temp,
#             "feels_like": feels_like,
#             "humidity": humidity,
#             "description": weather_desc
#         }

#     except requests.exceptions.Timeout:
#         print("Request timed out.")
#     except requests.exceptions.HTTPError as http_err:
#         print(f"HTTP error: {http_err}")
#     except requests.exceptions.RequestException as err:
#         print(f"Error: {err}")
#     except KeyError:
#         print("Unexpected response format.")
#     return None


# if __name__ == "__main__":
#     # Replace with your actual API key
#     API_KEY = "YOUR_API_KEY_HERE"
#     city_name = input("Enter city name: ").strip()

#     weather = get_weather(city_name, API_KEY)
#     if weather:
#         print(f"\nWeather in {weather['city']}:")
#         print(f"  {weather['description']}")
#         print(f"  Temperature: {weather['temperature']}°C")
#         print(f"  Feels like: {weather['feels_like']}°C")
#         print(f"  Humidity: {weather['humidity']}%")