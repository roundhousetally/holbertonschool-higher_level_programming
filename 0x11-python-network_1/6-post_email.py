#!/usr/bin/python3
""" sends a post request with data to url """
from sys import argv
import requests

if __name__ == "__main__":
    web = argv[1]
    form = {"email": argv[2]}
    req = requests.post(web, data=form)
    print(req.text)
