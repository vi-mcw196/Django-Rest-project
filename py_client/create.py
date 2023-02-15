import requests

headers = {'Authorization': 'Bearer 56be721aeecb0ed611e2765e9253e2d62f0badfc'}
endpoint = "http://127.0.0.1:8000/api/products/"

data = {
    "title": "This field is done"
}
get_response = requests.post(endpoint, json=data)
print(get_response.json())
