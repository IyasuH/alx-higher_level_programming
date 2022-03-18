#!/usr/bin/python3
import urllib.request
"""
A python script that fetches https://alx-intranet.hbtn.io/status
"""
with urllib.request.urlopen('https://alx-intranet.hbtn.io/status') as response:
    html = response.read()
    print("Body response:")
    print("    - type:", type(html))
    print("    - content:", html)
    print("    - utf8 content:", html.decode('utf-8'))
