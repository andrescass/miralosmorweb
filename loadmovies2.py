import json
import requests
import sys
import csv

def movieUpload(name, year, link, id, tags):
    cast = ''
    director = ''
    api_key = '4353298258a7759c4d87f81af0da6ce3'
    get_url = 'https://api.themoviedb.org/3/movie/' + id + '/credits?api_key=' + api_key
    mov = requests.get(get_url)
    mov_dict = mov.json()
    for i in range(0,5):
        cast += mov_dict['cast'][i]['name'] + ','
    for c in mov_dict['crew']:
        if c['job'] == 'Director':
            director = c['name']
    #print(mov_dict['cast'][0])
    
    sampleDict = {
        "name": name,
        "year": year,
        "director": director,
        "imdb_id": id,
        "cast": cast,
        "words": tags,
        "link" : link
    }
    jsonData = json.dumps(sampleDict)

    response = requests.post('http://miralosmorserver.pythonanywhere.com/api/movies', jsonData)

    print("{0} with code: {1}".format(name,response.status_code))

if __name__ == "__main__":
    if(len(sys.argv) < 3):
        print("Falta el nombre de archivo o los tags")
    else:
        fileN = sys.argv[1]
        tags = ""
        print("Leyendo el archivo {0}".format(fileN))
        for i in range(2,len(sys.argv)):
            tags += sys.argv[i] + " "
        
        with open(fileN, mode='r') as csv_file:
            csv_reader = csv.DictReader(csv_file, delimiter=',')
            line_count = 0
            for movie in csv_reader:
                movieUpload(movie["Name"], movie["Year"], movie["URL"], movie['imdb_id'], tags)
                line_count +=1
        print(f'Subidas {line_count} películas')
    

