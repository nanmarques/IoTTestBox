"""
This module contains a simple class modeling a Sensor.
"""


class Sensor:

    def __init__(self, id, name, value):
        self._id = id
        self._name = name
        self._value = value

    def get_prop(self, prop):
        if prop == "id":
            return self._id
        elif prop == "name":
            return self._name
        elif prop == "value":
            return self._value
        else:
            return None

    def set_prop(self, value):
        self._value=value
