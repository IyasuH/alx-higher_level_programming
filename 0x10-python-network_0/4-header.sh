#!/bin/bash
# Bash script that takes in a URL as an argument, sends a GET request to the URL, and displays the body of the response
curl -sX -H GET -G "$1" -d "X-School-User-Id=98"
