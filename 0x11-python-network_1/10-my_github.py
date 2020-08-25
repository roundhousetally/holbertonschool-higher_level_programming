#!/usr/bin/python3
""" script takes gh creds and uses the github api to display id """
from sys import argv
import requests


if __name__ == "__main__":
    web = "https://api.github.com/user"
    login = (argv[1], argv[2])
    resp = requests.get(web, auth=login)
    try:
        print(resp.json().get("id"))
    except ValueError:
        print("Not a valid JSON")
