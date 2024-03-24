import requests
from requests.exceptions import Timeout

try:
    response = requests.get("https://api.github.com", timeout=(3.05, 5))
except Timeout:
    print("The request timed out")
else:
    print("The request did not time out")

# first param of timeout Connect timeout: The time it allows for the client to establish a connection to the server
# second param of timeoutRead timeout: The time it’ll wait on a response once your client has established a connection