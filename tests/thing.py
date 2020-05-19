"""
This module contains a simple class modeling a Thing.
"""


class Thing:

    def __init__(self, id, token, name):
        self._id = id
        self._token = token
        self._name = name
        self._sensors = []

    def get_prop(self, prop):
        if prop == "id":
            return self._id
        elif prop == "token":
            return self._token
        elif prop == "name":
            return self._name
        elif prop == "sensors":
            return self._sensors
        else:
            return None

    def add_sensor(self, sensor):
        self._sensors.append(sensor)
