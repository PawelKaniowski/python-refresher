import requests

requests = requests.get("https://api.github.com", verify=False)
print(requests.text)
