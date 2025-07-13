import requests
from datetime import datetime, timedelta
from twilio.rest import Client
import json
import os

with open("api_keys.json", "r") as file:
    data = json.load(file)

appid = data["appid"]
account_sid = data["account_sid"]
auth_token = data["auth_token"]
number_to = data["number_to"]
number_from = data["number_from"]

parameters = {
    "lat": 14.5306,
    "lon": 121.0364,    # Manila, Philippines
    "cnt": 4,
    "appid": appid
}

client = Client(account_sid, auth_token)

response = requests.get(url="https://api.openweathermap.org/data/2.5/forecast", params=parameters)
# print(response.status_code)

weather_data = response.json()
# print("dt_txt", "\t\t\t", "weather_id", "\t", "description")

is_raining = False
for hour_time in weather_data["list"]:
    weather_id = hour_time["weather"][0]["id"]
    weather_time = datetime.strptime(hour_time["dt_txt"], '%Y-%m-%d %H:%M:%S') + timedelta(hours=8)  # Get only the date part
    # print(weather_time, "\t",
    #       weather_id, "\t\t",
    #       hour_time["weather"][0]["description"])
    if weather_id < 700:
        is_raining = True

message = f"[{weather_time.strftime('%A, %B %d, %Y')}]\nIt's going to rain today.\nBring an umbrella! ☔ "

if is_raining:
    print(message)
    message = client.messages.create(
        from_='whatsapp:' + number_from,
        body = message,
        to='whatsapp:' + number_to
    )