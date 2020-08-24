#!/usr/bin/python3
""" sends a req using requests """
import requests
from sys import argv
if __name__ == "__main__":
    web = argv[1]
    req = requests.get(web)
    print(req.headers.get("X-Request-Id"))
