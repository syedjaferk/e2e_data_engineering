import requests
from requests.adapters import HTTPAdapter
from urllib3.util.retry import Retry

BASE = "https://jsonplaceholder.typicode.com"

retry = Retry(
    total=5,  # at most 5 retries
    backoff_factor=1,  # waits about 1, 2, 4, 8… seconds
    status_forcelist=[429, 500, 502, 503, 504],  # retry only these
    allowed_methods=["GET"],  # never automatically repeat a POST
    respect_retry_after_header=True,
)
api = requests.Session()
api.mount("https://", HTTPAdapter(max_retries=retry))

counter = 0
while True:
    print(counter, api.get(f"{BASE}/users/3", timeout=10).json()["name"])
    counter += 1
