import requests
from pprint import pprint

url = "http://localhost:8000/participants/plan"  # Replace with the actual URL

response = requests.get(url)

pprint(response.json())