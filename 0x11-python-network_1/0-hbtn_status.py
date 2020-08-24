#!/usr/bin/python3
""" fetches the intranet status """
import urllib.request
if __name__ == "__main__":
    with urllib.request.urlopen("https://intranet.hbtn.io/status") as resp:
        b = resp.read()
        print("Body response:")
        print("\t- type: {}".format(type(b)))
        print("\t- content: {}".format(b))
        print("\t- utf8 content: {}".format(b.decode("utf-8")))
