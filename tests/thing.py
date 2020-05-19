"""
This module contains a simple class modeling a Thing.
"""


class Thing:

    def __init__(self, id, token, name):
        self._id = id
        self._token = token
        self._name = name

    def get_prop(self, prop):
        if prop == "id":
            return self._id
        elif prop == "token":
            return self._token
        elif prop == "name":
            return self._name
        else:
            return None
