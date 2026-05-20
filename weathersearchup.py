import requests
import tkinter as tk


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

def search_weather():
    city = city_entry.get()
    if city == "":
        result_label.config(text="Please enter a city name.")
        return

    result = getWeather(city)
    if result:
        result_label.config(
            text=
            f"Temperature: {result['temperature']}°C\n"
            f"Weather: {result['weather_descriptions'][0]}\n"
            f"Wind Speed: {result['wind_speed']} km/h\n"
            f"Humidity: {result['humidity']}%"
        )     
    else:
        result_label.config(text="Error fetching weather data.")

window = tk.Tk()
window.title("API Weather Search")
window.geometry("350x250")

city_label = tk.Label(window, text="Enter City Name:", font=("Arial", 12))
city_label.pack(pady=10)

city_entry = tk.Entry(window, font=("Arial", 12))
city_entry.pack(pady=10)

search_button = tk.Button(
    window,
    text="Get Weather",
    command=search_weather,
    font=("Arial", 14),
    bg="lightblue",
    fg="black",
    relief="raised",
    padx=10,
    pady=5
)

search_button.pack(pady=10)

result_label = tk.Label(window, text="", font=("Arial", 12))
result_label.pack(pady=20)

window.mainloop()

# def say_hello():
#     print("Hello there!")
# window = tk.Tk()
# window.title("Button Example")
# # Create the button
# my_button = tk.Button(
#     window, # parent container
#     text="Say Hello", # label text
#     command=say_hello, # function to call when clicked
#     font=("Arial", 16), # nice big font
#     bg="lightblue", # background color
#     fg="black", # text color
#     relief="raised", # gives it a 3D look
#     padx=10, pady=5 # padding around the text

# )
# my_button.pack(pady=20) # place it on the window
# window.mainloop()

# city = input("Enter a city: ")
# weather = getWeather(city)

# for k, x in weather.items():
#     print(f"{k.title()}: {x}")

