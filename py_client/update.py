import requests

endpoint = "http://localhost:8000/api/products/4/update/"

data = {
    "title" : 'Grey Tshirt',
    "content" : "this is real thing",
}

get_response = requests.put(endpoint, json=data)

print(get_response.status_code) 
print(get_response.json())