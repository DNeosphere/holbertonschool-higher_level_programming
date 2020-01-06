#!/bin/bash
# sends a request to that URL, and displays the size of the body of the response
curl -sI http://1e0a6b7ef075.20.hbtn-cod.io:5000 | grep Content-Length | cut -d ":" -f 2 | cut -d " " -f 2