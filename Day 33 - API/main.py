import requests

response = requests.get(url="http://api.open-notify.org/iss-now.json")    # Review JSON and HTTP status codes
# print(response.raise_for_status())

data = response.json()
longitude = data["iss_position"]["longitude"]
latitude = data["iss_position"]["latitude"]

position = (float(longitude), float(latitude))
print(position)