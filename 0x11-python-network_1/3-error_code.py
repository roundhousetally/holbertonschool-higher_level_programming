#!/usr/bin/python3
""" sends a post request with data to url """
from sys import argv
import urllib.request as r
import urllib.error as er


if __name__ == "__main__":
    web = argv[1]
    req = r.Request(web)
    try:
        with r.urlopen(req) as resp:
            print(resp.read().decode("ascii"))
    except er.HTTPError as e:
        print("Error code: {}".format(e.code))
