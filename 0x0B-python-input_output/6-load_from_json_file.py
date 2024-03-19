#!/usr/bin/python3
"""Create an object from a file Module"""
import json


def load_from_json_file(filename):
    """Creates an object from a JSON file"""
    with open(filename, 'r', encoding="utf-8") as f:
        return json.load(f)
