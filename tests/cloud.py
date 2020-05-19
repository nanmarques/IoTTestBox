"""
This module contains a simple class modeling a Cloud.
Things, Gateways or Apps may be added or removed from the Cloud.
"""
from tests.libs.terminal import run_script
import tests.libs.constants as constants


class Cloud:

    def __init__(self):
        self._gateways = []
        self._apps = []
        self._things = []

    def count(self, option="all"):
        if option == "all":
            return len(self._gateways) + len(self._apps) + len(self._things)
        elif option == "gateway":
            return len(self._gateways)
        elif option == "apps":
            return len(self._apps)
        elif option == "things":
            return len(self._things)
        else:
            return None

    def add(self, option, object):
        if option == "gateway":
            self._gateways.append(object)
            return True
        elif option == "thing":
            self._things.append(object)
            return True
        elif option == "app":
            self._apps.append(object)
            return True
        else:
            return False

    def connect(self, arguments):
        return run_script(constants.connect_script_path, arguments)
