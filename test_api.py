import requests

url = "http://127.0.0.1:5000/predict"

data = {
    "sl": 5.1,
    "sw": 3.5,
    "pl": 1.4,
    "pw": 0.2
}

response = requests.post(url, json=data)

print(response.json())