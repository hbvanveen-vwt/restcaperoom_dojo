import requests
import json

endpoint = "https://restcaperoom-api.test-app.vwtelecom.com"

print(f"Documentation of API: {endpoint}/ui")

response = requests.get(endpoint)
print(f"Getting {endpoint}: {json.dumps(response.json(), indent=2)}")
