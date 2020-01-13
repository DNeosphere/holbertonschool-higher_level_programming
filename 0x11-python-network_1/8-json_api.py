#!/usr/bin/python3
import requests
from sys import argv

if __name__ == "__main__":

    try:
        dato = {'q': argv[1]}
    except Exception:
        dato = {'q': ""}
        pass

    try:
        req = requests.post('http://0.0.0.0:5000/search_user', data=dato)
        req_json = req.json()
        if 'id' not in req_json or 'name' not in req_json:
            print("No result")
        else:
            print("[{}] {}".format(req_json.get('id'), req_json.get('name')))

    except Exception:
            print("Not a valid JSON")
