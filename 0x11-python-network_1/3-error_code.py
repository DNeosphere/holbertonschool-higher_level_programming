#!/usr/bin/python3
import urllib
from urllib import request
from sys import argv

if __name__ == "__main__":
    try:
        with request.urlopen(argv[1]) as resp:
            info = resp.read()
            print(info.decode('utf-8'))
    except urllib.error.HTTPError as err:
        print('Error code: {}'.format(err.code))
