#!/usr/bin/python3
"""Student Class Module"""


class Student:
    """Represnts a student"""
    def __init__(self, first_name, last_name, age):
        """Initializes a the sudent class"""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """retrieves a dictionary representation of a Student instance"""
        if attrs is None:
            return self.__dict__
        attr_dict = {}
        for attr in attrs:
            try:
                attr_dict[attr] = self.__dict__[attr]
            except Exception:
                pass
        return attr_dict

    def reload_from_json(self, json):
        """Replaces all attributes of the Student instance using data
        from the json"""
        for key, value in json.items():
            try:
                self.key = value
            except Exception:
                pass
