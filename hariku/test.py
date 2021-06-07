import json

with open("hariku/keywords.json",) as keywords:
    for data in json.load(keywords)['positive']:
        print(data)