import requests

endpoint = "http://localhost:8000/api/"

get_response = requests.post(endpoint, json = {"title": "Hari", "content" : "hello world"})

print(get_response.status_code) 
print(get_response.json())