import json
import requests

sampleDict = {
    "name": "Movie3",
    "words":"corchazo bajon",
    "link" : "movie3"
}
jsonData = json.dumps(sampleDict)

response = requests.post('http://miralosmorserver.pythonanywhere.com/api/movies', jsonData)

print(response.status_code)