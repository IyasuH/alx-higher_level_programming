#!/usr/bin/python3
"""
A python script that fetches https://alx-intranet.hbtn.io/status
"""
if __name__ == "__main__":
    import requests
    html = requests.get('https://alx-intranet.hbtn.io/status')
    print("Body response:")
    print("\t- type:", type(html.text))
    print("\t- content:", html.text)
