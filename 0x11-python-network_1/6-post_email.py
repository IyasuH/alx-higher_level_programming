#!/usr/bin/python3
"""
Python script that takes in a URL and an email address, sends
a POST request to the passed URL with the email as a parameter,
and finally displays the body of the response
"""
if __name__ == "__main__":
    import requests
    import sys
    mail = {'Your email is': sys.argv[2]}
    email = requests.post(sys.argv[1], data=mail)
    print(email.text)
