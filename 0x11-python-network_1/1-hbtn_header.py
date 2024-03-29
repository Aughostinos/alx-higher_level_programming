#!/usr/bin/python3
"""Python script that takes in a URL, sends a request to the URL   and displays the value of the X-Request-Id variable found in
   the header of the response."""


import urllib.request
import sys


url = sys.argv[0]

req = urllib.request.Request(url)
with urllib.request.urlopen(req) as response:
	headers = response.info()
	x_req_id = headers.get('X-Request-Id')

print(x_req_id)
