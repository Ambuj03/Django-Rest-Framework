import requests

endpoint = "http://localhost:8000/api/products/4/"

get_response = requests.get(endpoint, json = {"title": "Hari", "content" : "hello world"})

print(get_response.status_code) 
print(get_response.json())