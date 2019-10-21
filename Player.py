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

# Li said the inheritance relationship  is wrong, so I comment it out

# class Player1(Player):
#     # a variable to store num of tokens for each player
#     tokenP1 = 15
#     visitedCoordinatesP1 = [Coordinates(0,3), Coordinates(0,0), Coordinates(0,2), Coordinates(2,0), Coordinates(2,2), Coordinates(3,4), Coordinates(4,0)] #It contains the needed coordinates to let the middle coordinates(1,1) win
#
#     def __init__(self, owner, shape, x, y):
#         super().__init__(owner, shape, x, y)
#         self.owner = owner
#         self.shape = shape
#
#     @classmethod
#     def constructor(self, token):
#         self.token = token
#
#     @classmethod
#     def getVisitedCoordinates(self):
#         return self.visitedCoordinatesP1
#
#     def printCoordinates(self):
#         # super().getCoordinates(self)
#         print(self.owner + '\'s coordinates is: (' + self.token.coordinates.x + ',' + self.token.coordinates.y +')')


# class Player2(Player):
#     # a variable to store num of tokens for each player
#     tokenP2 = 15
#     visitedCoordinatesP2 = []
#     tokenListP2 = []
#
#     def __init__(self, owner, shape, x, y):
#         super().__init__(owner, shape, x, y)
#         self.owner = owner
#         self.shape = shape
#
#     def constructor(self, token):
#         self.token = token
#
#     def getVisitedCoordinates(self):
#         return self.visitedCoordinatesP2
#
#     def printCoordinates(self):
#         # super().getCoordinates(self)
#         print(self.owner + '\'s coordinates is: (' + self.token.coordinates.x + ',' + self.token.coordinates.y + ')')


# # some testing cases
# p1 = Player('Player1','X', '3', 'A')
# p2 = Player2('Player2','~', '4', 'B')
# p1.printCoordinates()
# p2.printCoordinates()
#


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
