import requests

AMOUNT = 10
DIFFICULTY = "easy"

parameters = {
    "amount": AMOUNT,
    "difficulty": DIFFICULTY,
    "type": "boolean"
}

response = requests.get(url="https://opentdb.com/api.php", params=parameters)
response.raise_for_status()
question_data = response.json()["results"]