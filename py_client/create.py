import requests

endpoint = "http://localhost:8000/api/products/"

get_response = requests.post(endpoint, json = {"title": "Blue one", "content" : "Nice!!!!!!!!!!"})

print(get_response.status_code) 
print(get_response.json())