import requests

url = 'http://0.0.0.0:8910/predict'

customer = {"contract": "two_year", "tenure": 1, "monthlycharges": 10}

response = requests.post(url, json=customer).json()
print(response) 