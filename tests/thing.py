"""
This module contains a simple class modeling a Thing.
"""


class Thing:

    def __init__(self, id, token, name):
        self._id = id
        self._token = token
        self._name = name
