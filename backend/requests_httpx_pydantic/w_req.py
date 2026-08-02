import requests

response = requests.get("https://jsonplaceholder.typicode.com/posts/1")

print(response.json())
print(response.text)
print(response.status_code)
print(response.json())
