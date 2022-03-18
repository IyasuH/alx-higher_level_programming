#!/usr/bin/python3
"""
Python script that takes in a URL and an email, sends
a POST request to the passed URL with the email as a parameter,
and displays the body of the response
"""
if __name__ == "__main__":
    import urllib.request
    import urllib.parse
    import sys
    values = {'email' : sys.argv[2]}
    data = urllib.parse.urlencode(values)
    data = data.encode('utf-8')
    req = urllib.request.Request(sys.argv[1], data)
    with urllib.request.urlopen(req) as response:
        page = response.read()
        print("Your email is: ", page.decode('utf-8'))
