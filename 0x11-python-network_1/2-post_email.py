#!/usr/bin/python3
from urllib import parse
from urllib import request
from sys import argv

if __name__ == "__main__":
    url = argv[1]
    value = {'email': argv[2]}
    data = parse.urlencode(value)
    data = data.encode('ascii')
    req = request.Request(url, data)
    with request.urlopen(req) as response:
        the_page = response.read()
        print(the_page.decode('utf-8'))
