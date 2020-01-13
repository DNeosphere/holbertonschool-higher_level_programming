#!/usr/bin/python3
import requests
from sys import argv
from requests.exceptions import HTTPError

if __name__ == "__main__":
    req = requests.get(argv[1])
    if req.status_code > 400:
        print('Error code: {}'.format(req.status_code))
    else:
        print(req.text)
