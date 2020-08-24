#!/usr/bin/python3
""" takes in url and sends a request to url for x-reuqest-id var """
import urllib.request as r
from sys import argv
if __name__ == "__main__":
    with r.urlopen(r.Request(argv[1])) as resp:
        print(resp.headers.get("X-Request-Id"))
