import json
import requests
import sys
import csv

def movieUpload(name, year, link, id, tags):
    api_key = '4353298258a7759c4d87f81af0da6ce3'
    get_url = 'https://api.themoviedb.org/3/movie/' + id + '/credits?api_key=' + api_key
    mov = requests.get(get_url)
    mov_dict = mov.json()
    for i in range(0,5):
        print(mov_dict['cast'][i]['name'])
    for c in mov_dict['crew']:
        if c['job'] == 'Director':
            print(c['name'])
    #print(mov_dict['cast'][0])
    
    # sampleDict = {
    #     "name": name,
    #     "year": year,
    #     "words": tags,
    #     "link" : link
    # }
    # jsonData = json.dumps(sampleDict)

    # response = requests.post('http://miralosmorserver.pythonanywhere.com/api/movies', jsonData)

    # print("{0} with code: {1}".format(name,response.status_code))

if __name__ == "__main__":
    movieUpload('Frida', 1990, 'lala', 'tt3774694', 'lalala')

