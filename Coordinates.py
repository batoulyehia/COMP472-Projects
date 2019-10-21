# reference : __eq__ https://stackoverflow.com/questions/1227121/compare-object-instances-for-equality-by-their-attributes-in-python

class Coordinates:

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __eq__(self, other):
        if not isinstance(other, Coordinates):
            # don't attempt to compare against unrelated types
            return NotImplemented
        return self.x == other.x and self.y == other.y

    def printCoordinate(self):
        print("X: " + str(self.x) + " Y: " + str(self.y))

# list = []
#
# for x in range(ord('A'), ord('M') + 1):
#     for y in range(1, 11):
#         list.append((chr(x), y))
