#!/usr/bin/python3
import urllib.request
import sys
"""
A python script thta takes in a URL sends a request to the URL and displays the value of the
X-Request-Id variable found in the header of the response
"""
req = urllib.request.Request(sys.argv[1])
with urllib.request.urlopen(req) as response:
    html = response.read()
    req.get_header('X-Request-Id')

