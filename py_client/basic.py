import requests

endpoint = "http://127.0.0.1:8000/"
endpoint2 = "https://httpbin.org/status/200"

get_response = requests.get(endpoint)  # HTTP request
print(get_response.text)
# print(get_response.json())
