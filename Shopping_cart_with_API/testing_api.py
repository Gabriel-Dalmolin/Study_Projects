import requests


# requests.post("http://127.0.0.1:8000/add", json={"name": "tomato", "price": 5})
response = requests.get("http://127.0.0.1:8000/cart")

print(response.json())