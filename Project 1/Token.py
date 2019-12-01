# reference : __eq__ https://stackoverflow.com/questions/1227121/compare-object-instances-for-equality-by-their-attributes-in-python
from Coordinates import *


class Token:
    def __init__(self, owner, shape, x, y):
        self.owner = owner
        self.shape = shape
        self.coordinates = Coordinates(x, y)

    def getCoordinates(self):
        return self.coordinates.x, self.coordinates.y

    def __eq__(self, other):
        if not isinstance(other, Token):
            # don't attempt to compare against unrelated types
            return NotImplemented

        return self.coordinates.x == other.coordinates.x and self.coordinates.y == other.coordinates.y
