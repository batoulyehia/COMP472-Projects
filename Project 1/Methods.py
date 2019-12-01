from Coordinates import *
import re
from Token import *
from Player import *


# split the user entered string into two parts: alphabetic part and numerical part. A1 will be A->temp[0] 1->temp[1]

def toRealCoordinates(temp):
    if (bool(re.search('[a-zA-Z]', temp[1:]))):
        raise Exception(
            "illegal input, you have to enter the alphabetic part (A to L) and numerical part (1 to 10) in order")
    if 65 <= ord(temp[0]) <= 76 and 1 <= int(temp[1:]) <= 10:
        y = ord(temp[0]) - 65  # starting from 0
        x = int(temp[1:]) - 1  # starting from 0

        reversedX = 9 - x
        print('x: ' + str(reversedX) + '  ' + 'y: ' + str(y))
        return Coordinates(reversedX, y)
    raise Exception(
        "illegal input, you have to enter the alphabetic part (A to L) and numerical part (1 to 10) in order")


def doIWin(currentplayer , otherPlayer):
    # check on all tokens of currentplayer
    victoryStatus = False
    if not victoryStatus:
        for currentToken in currentplayer.tokenList:
            isEdge = checkEdge(currentToken)
            isMiddle = findMiddle(currentToken, isEdge, currentplayer)
            isHorizontal = checkHorizontal(currentToken, isEdge, isMiddle, otherPlayer)
            victoryStatus = checkWin(isMiddle, isHorizontal)
            if victoryStatus:
                return True
    else:
        return False


def findMiddle(token, check, player):
    if not check:
        x, y = token.getCoordinates()
        # store all the necessary moves needed to win except the middle at the current token
        upLeft = Coordinates(x - 1, y - 1)
        upRight = Coordinates(x - 1, y + 1)
        downLeft = Coordinates(x + 1, y - 1)
        downRight = Coordinates(x + 1, y + 1)

        neededTokenToWin = [upLeft, upRight, downLeft, downRight]

        visitedList = []

        p1Visited = player.getVisitedCoordinates()
        for i in range(len(p1Visited)):
            visitedList.append(p1Visited[i])

        counter = 0
        for i in visitedList:
            for j in neededTokenToWin:
                if i == j:
                    counter += 1
                    continue
        if counter == 4:  # It should make sure that the visitedList has no duplicated coordinates since logically it should not happen
            # print('Middle found')
            return True
        else:
            # print('Middle not found')
            return False
    else:
        # print('Middle not found')
        return False


# Testing cases, it returns True
# tokenP1 = Token('P1','X', 1, 1)
#
# print(findMiddle(tokenP1, False))
# toRealCoordinates('A10').printCoordinate()

# Determines if the current token is an edge or not
# For victory condition this must return false
def checkEdge(token):
    x, y = token.getCoordinates()
    # this gives different edges for current grid so commented them out
    # up = Coordinates(x, y + 1)
    # down = Coordinates(x, y - 1)
    # left = Coordinates(x - 1, y)
    # right = Coordinates(x + 1, y)

    # edges in the current gird are x=0, x=9, y=0, y=11
    if x >= 9 or x < 1 or y < 1 or y >= 11:
        # print('Edge is True')
        return True
    else:
        # print('Edge is False')
        return False


# Test cases
# print(checkEdge(Token('player1','x',0,6))) #is an edge, returns true
# print(checkEdge(Token('p2','O',4,5))) #is not an edge, returns false

def checkWin(checkMiddle, checkHorizontal):
    if checkMiddle and checkHorizontal:
        return True

# checks for adversary right and left to middle token
def checkHorizontal(currentToken, isEdge, isMiddle, otherPlayer):
    # if it is edge then no need to check left or right condition
    if isEdge or not isMiddle:
        # print('from checkHorizontal: isEdge: ' + str(isEdge) + ' isMiddle: ' + str(isMiddle))
        return False

    x, y = currentToken.getCoordinates()
    # print(currentToken.owner)
    # print('Current x: ' + str(x) + '  ' + 'y: ' + str(y))

    # x, y coordinates of left cell from currentToken
    # this should be the actual left coords but because grid is behaving different/reverse therefore y values changes.
    # leftX = x - 1
    # leftY = y
    leftX = x
    leftY = y - 1
    # print('Left x: ' + str(leftX) + '  ' + 'y: ' + str(leftY))

    # x, y coordinates of right cell from currentToken
    # rightX = x + 1
    # rightY = y
    rightX = x
    rightY = y + 1
    # print('Right x: ' + str(rightX) + '  ' + 'y: ' + str(rightY))

    otherPlayervisitedCoordinates = otherPlayer.visitedCoordinates

    for left_coords in otherPlayervisitedCoordinates:
        adversary_x = left_coords.x
        adversary_y = left_coords.y
        # print('OtherPlayer: x: ' + str(adversary_x) + '  ' + 'y: ' + str(adversary_y))
        # check whether the left coordinates are from other player or not
        if leftX == adversary_x and leftY == adversary_y:
            # print('Adversary on left exists:  x: ' + str(adversary_x) + '  ' + 'y: ' + str(adversary_y))
            # if true then check the other side
            for right_coords in otherPlayervisitedCoordinates:
                adversary_x = right_coords.x
                adversary_y = right_coords.y
                if rightX == adversary_x and rightY == adversary_y:
                    # print('Adversary on right exists:  x: ' + str(adversary_x) + '  ' + 'y: ' + str(adversary_y))
                    return False

    # if you get here it means no/1 adversary tokens on the horizontal coordinates
    # print('None or 1 adversary tokens on the horizontal coordinates')
    return True
