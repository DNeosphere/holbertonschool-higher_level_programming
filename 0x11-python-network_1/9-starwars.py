#!/usr/bin/python3
import requests
from sys import argv

if __name__ == "__main__":

    value = {'search': argv[1]}
    req = requests.get("https://swapi.co/api/people/", params=value)

    req_json = req.json()
    print("Number of results: {}".format(req_json.get('count')))
    list = req_json.get('results')
    for res in list:
        print(res.get('name'))
