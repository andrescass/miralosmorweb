import json
import requests

sampleDict = {
    "name": "Movie4",
    "words":"corchazo bajon",
    "link" : "movie3"
}
jsonData = json.dumps(sampleDict)

response = requests.post('http://localhost:8000/api/movies', jsonData)

print(response.status_code)