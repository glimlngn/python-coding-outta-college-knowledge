import requests

with open("api_key.txt", "r") as file:
    SUPER_SECRET_API_KEY = file.read()

LAT = 14.5306
LON = 121.0364

parameters = {
    "lat": LAT,
    "lon": LON,
    "appid": SUPER_SECRET_API_KEY
}

response = requests.get(url="https://api.openweathermap.org/data/2.5/forecast", params=parameters)
print(response.status_code)

weather_data = response.json()
print("dt_txt", "\t\t\t", "weather_id", "\t", "description")
for datetime in weather_data["list"]:
    print(datetime["dt_txt"], "\t", 
          datetime["weather"][0]["id"], "\t\t", 
          datetime["weather"][0]["description"])