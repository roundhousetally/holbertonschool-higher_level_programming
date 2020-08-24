#!/usr/bin/python3
""" sends a post request with data to url """
from sys import argv
import urllib.parse as p
import urllib.request as r


if __name__ == "__main__":
    web = argv[1]
    form = {'email': argv[2]}
    data = p.urlencode(form).encode("ascii")
    req = r.Request(web, data)
    with r.urlopen(req) as resp:
        print(resp.read().decode("uft-8"))
