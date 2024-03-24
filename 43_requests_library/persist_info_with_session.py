import requests

from custom_token_auth import TokenAuth

TOKEN = "<YOUR_GITHUB_PA_TOKEN>"

with requests.Session() as session:
    session.auth = TokenAuth(TOKEN)

    first_response = session.get("https://api.github.com/user")
    second_response = session.get("https://api.github.com/user")

print(first_response.headers)
print(second_response.json())

import requests

token = "<YOUR_GITHUB_PA_TOKEN>"
response = requests.get(
    "https://api.github.com/user",
    auth=("", token)
)
print(response.status_code)