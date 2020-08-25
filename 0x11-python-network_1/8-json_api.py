#!/usr/bin/python3
""" takes in a letter and sends a post req with letter as param """
import requests
from sys import argv


if __name__ == "__main__":
    if len(argv) == 1:
        l = ""
    else:
        l = argv[1]
    f = {"q": l}
    web = "http://0.0.0.0:5000/search_user"
    req = requests.post(web, data=f)
    try:
        r = req.json()
        if r == {}:
            print("No result")
        else:
            print("[{}] {}".format(r.get("id"), r.get("name")))
    except ValueError:
        print("Not a valid JSON")
