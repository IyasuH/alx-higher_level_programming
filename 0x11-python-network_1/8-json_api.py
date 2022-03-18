#!/usr/bin/python3
"""
Python script that takes in a letter and sends
a POST request to http://0.0.0.0:5000/search_user
with the letter as a parameter
"""
if __name__ == "__main__":
    import requests
    import sys
    if sys.argv[2]:
        x = request.post(sys.argv[1], q=sys.argv[2])
        j = x.json()
    else:
        x = request.post(sys.argv[1], q="")
        j = x.json()
    try:
        r = json.loads(j)
        if r == "":
            print("No result")
        else:
            print(r)
    except:
        print("Not a valid JSON")
