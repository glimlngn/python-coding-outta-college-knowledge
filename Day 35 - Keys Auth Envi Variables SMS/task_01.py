import requests

with open("api_key.txt", "r") as file:
    SUPER_SECRET_API_KEY = file.read()

parameters = {
    "lat": 14.5306,
    "lon": 121.0364,    # Manila, Philippines
    "appid": SUPER_SECRET_API_KEY
}

response = requests.get(url="https://api.openweathermap.org/data/2.5/forecast", params=parameters)
print(response.status_code)

weather_data = response.json()
print("dt_txt", "\t\t\t", "weather_id", "\t", "description")
for hour_time in weather_data["list"]:
    print(hour_time["dt_txt"], "\t", 
          hour_time["weather"][0]["id"], "\t\t", 
          hour_time["weather"][0]["description"])