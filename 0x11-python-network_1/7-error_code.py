#!/usr/bin/python3
""" sends a post request with data to url """
from sys import argv
import requests


if __name__ == "__main__":
    web = argv[1]
    req = requests.get(web)
    if req.status_code >= 400:
        print("Error code: {}".format(req.status_code))
    else:
        print(req.text)
