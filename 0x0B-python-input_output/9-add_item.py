#!/usr/bin/python3
""" adds all arguments to a python list and saves them to a file """
import sys
sj = __import__('7-save_to_json_file').save_to_json_file
lj = __import__('8-load_from_json_file').load_from_json_file
""" adding to list """
try:
    new_list = lj("add_item.json")
except:
    new_list = []
new_list.extend(sys.argv[1:])
sj(new_list, "add_item.json")
