#!/usr/bin/python3
"""
Python script that takes in a letter and sends
a POST request to http://0.0.0.0:5000/search_user
with the letter as a parameter
"""
if __name__ == "__main__":
    import requests
    import sys
    url = 'http://0.0.0.0:5000/search_user'
    if len(sys.argv) > 1: 
        q = requests.post(url, sys.argv[1])
    else:
        q = requests.post(url, "")
    try:
        r = q.json()
        if r == "":
            print("No result")
        else:
            print("[{}] {}".format(r.id, r.name))
    except ValueError:
        print("Not a valid JSON")
