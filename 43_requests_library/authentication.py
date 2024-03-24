import requests

response = requests.get(
    "https://httpbin.org/basic-auth/user/passwd",
    auth=("user", "passwd")
)

print(response.status_code)
print(response.request.headers["Authorization"])

from requests.auth import HTTPBasicAuth

r = requests.get(
    "https://httpbin.org/basic-auth/user/passwd",
    auth=HTTPBasicAuth("user", "Pawel")
)
print(r.status_code)
print(r.request.headers["Authorization"])
