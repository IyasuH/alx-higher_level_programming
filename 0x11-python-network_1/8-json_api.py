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
    if sys.argv[1]:
        q = request.post(url, sys.argv[1])
        j = q.json()
    else:
        q = ""
        j = q.json()
    try:
        r = json.loads(j)
        if r == "":
            print("No result")
        else:
            print("[{}] {}".format(r.id, r.name))
    except ValueError:
        print("Not a valid JSON")
