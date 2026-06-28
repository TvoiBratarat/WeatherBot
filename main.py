import requests
from datetime import datetime

API_KEY = "e75a310ae2db0270ef0849c7ed6727b2" 
CITY = input("Enter city name, case sensitive:")

current_url = f"http://api.openweathermap.org/data/2.5/weather?q={CITY}&appid={API_KEY}&units=metric"

current_response = requests.get(current_url)
current_data = current_response.json()

if current_data.get("cod") != 200:
    print(f"Error! City '{CITY}' not found.")
else:
    print(f"--- CURRENT WEATHER IN {CITY.upper()} ---")
    description = current_data['weather'][0]['description']
    temp = current_data['main']['temp']
    humidity = current_data['main']['humidity']
    wind_speed = current_data['wind']['speed']

    print(f"Condition: {description.capitalize()}")
    print(f"Temperature: {temp} °C")
    print(f"Humidity: {humidity}%")
    print(f"Wind speed: {wind_speed} m/s")
    print("\n")

forecast_url = f"http://api.openweathermap.org/data/2.5/forecast?q={CITY}&appid={API_KEY}&units=metric"

forecast_response = requests.get(forecast_url)
forecast_data = forecast_response.json()

if forecast_data.get("cod") != "200":
    print("Could not get forecast.")
else:
    print(f"--- 12-HOUR FORECAST ---")
    for item in forecast_data['list'][:4]:
        dt_txt = item['dt_txt']
        dt_obj = datetime.strptime(dt_txt, '%Y-%m-%d %H:%M:%S')
        pretty_time = dt_obj.strftime('%H:%M')
        
        hour_temp = item['main']['temp']
        hour_desc = item['weather'][0]['description']
        
        print(f"[{pretty_time}]: {hour_temp} °C, {hour_desc}")

print("\n--- End of script ---")