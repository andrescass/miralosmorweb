import json
import requests
import sys
import csv

def movieUpload(name, year, link, tags):
    sampleDict = {
        "name": name,
        "year": year,
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
            csv_reader = csv.DictReader(csv_file)
            line_count = 0
            for movie in csv_reader:
                movieUpload(movie["Name"], movie["Year"], movie["URL"], tags)
                line_count +=1
        print(f'Subidas {line_count-1} películas')