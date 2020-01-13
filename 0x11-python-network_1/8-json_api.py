#!/usr/bin/python3
import requests
from sys import argv

if __name__ == "__main__":

    try:
        dato = {'q': argv[1]}
    except:
        dato = {'q': ""}
        pass

    req = requests.post('http://0.0.0.0:5000/search_user', data=dato)
    req_json = req.json()

    if len(req_json) == 0:
        print("No result")

    else:
        try:
            print("[{}] {}".format(req_json['id'], req_json['name']))
        except Exception:
            print("Not a valid JSON")
