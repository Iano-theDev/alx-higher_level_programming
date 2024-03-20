#!/usr/bin/python3
"""Save argument list to file module"""
import sys
save_json_file = __import__("5-save_to_json_file").save_to_json_file
load_json = __import__("6-load_from_json_file").load_from_json_file
argList = []

for arg in sys.argv:
    argList.append(arg)
save_json_file(argList[1:], "add_item.json")
load_json("add_item.json")
