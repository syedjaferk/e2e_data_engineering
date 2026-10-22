import requests

url = "https://jsonplaceholder.typicode.com/posts/1"
response = requests.get(url)
print(response, dir(response))
print(response.json())

BASE = "https://jsonplaceholder.typicode.com"

r = requests.post(
    f"{BASE}/posts",
    json={"title": "pipeline finished", "body": "12 rows", "userId": 1},
    timeout=10,
)
print(r.status_code, r.json())
