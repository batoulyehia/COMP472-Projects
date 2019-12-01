import Methods
from Token import *


class Player(object):

    def __init__(self, owner, shape):
        # self.coordinates = Coordinates(x,y)
        # self.token = Token(owner, shape, x, y)
        self.owner = owner
        self.shape = shape
        # a variable to store num of tokens for player
        self.token = 15
        # It contains the needed coordinates to let the middle coordinates(1,1) win
        self.visitedCoordinates = []
        self.tokenList = []

    def constructToken(self, token):
        self.token = token

    def getVisitedCoordinates(self):
        return self.visitedCoordinates

    def gettokenList(self):
        return self.tokenList

    def getCoordinates(self):
        return self.token.coordinates.x, self.token.coordinates.y

    def printCoordinates(self):
        print(self.owner + '\'s coordinates is: (' + self.token.coordinates.x + ',' + self.token.coordinates.y + ')')

    # using this method to print visitedCoordinatesP1
    def printVisitedCoordianates(self):
        visitedCoordinatesList = self.getVisitedCoordinates()
        for i in visitedCoordinatesList:
            print('x: ' + str(i.x) + '  ' + 'y: ' + str(i.y))

    # put a token's coordinates into visitedCoordinatesP1
    def placeToken(self, token):
        coordinates = Coordinates(token.coordinates.x, token.coordinates.y)
        self.visitedCoordinates.append(coordinates)

    def removeTokenCoordinates(self, token):
        coordinates = token.coordinates
        self.visitedCoordinates.remove(coordinates)

    def addTokenToList(self, token):
        self.tokenList.append(token)

    def removeFromTokenList(self, token):
        self.tokenList.remove(token)

# # some testing cases
# p1 = Player('Player1','X', '3', 'A')
# p1.printCoordinates()

# a = Methods.toRealCoordinates('A2')
# a.printCoordinate()
# Coordinates.toRealCoordinates('A1')
# # bad cases
# # Coordinates.toRealCoordinates('0')
# # Coordinates.toRealCoordinates('AA')
# # Coordinates.toRealCoordinates(' ')
# # Coordinates.toRealCoordinates('M')


# p1 = Player('Player1','X')
# # before place a token's coordinates into the visitedCoordinatesP1
# p1.printVisitedCoordianates()
# print("=============================================================")
# # # after place a token's coordinates into the visitedCoordinatesP1
# p1.placeToken(Token('Player1','X', '3', 'A'))
# p1.printVisitedCoordianates()
# Methods.toRealCoordinates()
