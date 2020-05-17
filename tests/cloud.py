"""
This module contains a simple class modeling a Cloud.
Things, Gateways or Apps may be added or removed from the Cloud.
"""


class Cloud:

    def __init__(self):
        self._gateways = dict()
        self._apps = dict()
        self._things = dict()

    def count(self, option="all"):
        if option == "all":
            return len(self._gateways) + len(self._apps) + len(self._things)
        elif option == "gateway":
            return len(self._gateways)
        elif option == "apps":
            return len(self._apps)
        elif option == "things":
            return len(self._things)
        else
            return None


    def add(self, count=1):
        new_count = self.count + count
        if new_count > self.max_count:
            raise ValueError("Attempted to add too many cucumbers")
        self._count = new_count

    def remove(self, count=1):
        new_count = self.count - count
        if new_count < 0:
            raise ValueError("Attempted to remove too many cucumbers")
        self._count = new_count
