import sys

from Player import *
import string
import time


# Get token coordinates from user input
def getTokenCoordinates(board, playerName):
    while True:
        try:
            stringCoordinate = input(
                "\n%s, Please enter your coordinate and place your token (EX : A2)\n" % playerName)
            # Parse string to numbers
            numberCoordinate = Methods.toRealCoordinates(stringCoordinate)
            # Get coordinate x and y
            x = numberCoordinate.x
            y = numberCoordinate.y
            # Check if the cell occupied
            if isTheCellOccupied(board, x, y):
                print("The cell is already occupied, please enter another coordinates")
            else:
                return x, y
                break
        except Exception as e:
            print(
                "illegal input, you have to enter the alphabetic part (A to L) and numerical part (1 to 10) in "
                "order\nTry again")


# Print current board
def printBoard(board):
    tempNumber = 10
    alphabet = list(string.ascii_uppercase[0:12])
    for cell in alphabet:
        print(cell, end=" ")
    print()
    for cells in board:
        print(" ".join(map(str, cells)), end=" " + str(tempNumber))
        print()
        tempNumber = tempNumber - 1


# Check the cell occupied or not
def isTheCellOccupied(board, x, y):
    if board[x][y] != '_':
        return True
    else:
        return False


# Add the token on board
def addToBoard(board, x, y, shape):
    board[x][y] = shape


def removeFromBoard(board, x, y):
    board[x][y] = '_'


# Function that removes old token and old token coordinates from list and appends new ones
def move(player, shape, newToken, oldToken):
    # Take in the player input, parse the input into coordinates
    oldCoordinates = oldToken.getCoordinates()
    print("oldCoordinates" + str(oldCoordinates))
    newCoordinates = newToken.getCoordinates()
    print("newCoordinates" + str(newCoordinates))

    x1 = oldToken.coordinates.x
    y1 = oldToken.coordinates.y
    oldCoordinates = Coordinates(x1, y1)
    print(oldCoordinates.x)
    print(oldCoordinates.y)

    player.removeTokenCoordinates(oldToken)
    player.removeFromTokenList(oldToken)

    player.placeToken(newToken)
    player.addTokenToList(newToken)


def evaluateMove(token, userInput, player, board):
    print(userInput)
    x = token.coordinates.x
    y = token.coordinates.y
    isValid = False
    print(x)
    print(y)
    while isValid == False:
        if userInput == "UP":
            x = x - 1
        elif userInput == "DOWN":
            x = x + 1
        elif userInput == "LEFT":
            y = y - 1
        elif userInput == "RIGHT":
            y = y + 1
        elif userInput == "UP-LEFT":
            x = x - 1
            y = y - 1
        elif userInput == "UP-RIGHT":
            x = x - 1
            y = y + 1
        elif userInput == "DOWN-LEFT":
            x = x + 1
            y = y - 1
        elif userInput == "DOWN-RIGHT":
            x = x + 1
            y = y + 1
        print(x)
        print(y)

        if (x < 0) or (x > 9) or (y < 0) or (y > 11):
            print("Space is occupied. Please select another move.")
            userInput = input(
                "\n%s, Which way do you want to move?\nLEFT\nRIGHT\nUP\n\DOWN\nUP-LEFT\nUP-RIGHT\nDOWN-LEFT\nDOWN-RIGHT"
            )
            # reset values of x and y
            x = token.coordinates.x
            y = token.coordinates.y

        else:
            isValid = True
            return Token(token.owner, token.shape, x, y)


# TODO: REMOVE
def checkValidity(newToken, board):
    x = newToken.coordinates.x
    y = newToken.coordinates.y

    print('checking newToken in checkValidity x :' + str(x) + 'y:' + str(y))
    if (isTheCellOccupied(board, x, y)) or (x < 0) or (x > 9) or (y < 0) or (y > 11):
        return False
    else:
        return True


def startTwoPlayerGame():
    ##############Initalize the game##################
    # Create a 12*10 chess board which will place token
    # Reference:
    # How to create nested array
    # https://www.geeksforgeeks.org/python-using-2d-arrays-lists-the-right-way/
    board = [['_' for i in range(12)] for j in range(10)]
    print("Let's start two player game model\n")

    # Player1 setting
    player1Name = input("Player1\nPlease enter your name:\n")
    while not player1Name:
        player1Name = input("Invalid entry\nPlayer1\nPlease enter your name:\n")
    # Player1 default setting is X
    player1 = Player(player1Name, "X")

    # Player2 setting
    player2Name = input("Player2\nPlease enter your name:\n")
    while not player2Name:
        player2Name = input("Invalid entry\nPlayer2\nPlease enter your name:\n")
    # Player2 default setting is O
    player2 = Player(player2Name, "O")
    print("Thank you, and let's start the game.\nThis is our initial empty board\n")

    ##############game start##################
    # Create a counter for maximum 30 turns
    totalCounter = 30
    currentCounter = 0
    # print current board
    printBoard(board)
    # initialize the coordinates
    x = 0
    y = 0
    while totalCounter > 0:
        print("\nRound " + str(currentCounter + 1))  # Print the current round

        # Player1 start to play
        player1Choice = ""
        if currentCounter == 0:  # if it is first round, the default select is place
            player1Choice = "P"
        else:
            while True:  # this while loop is for determine the inputs valid or not
                player1Choice = input(
                    "\n%s, Please select what you want to do:\nMOVE(M) OR PLACE(P)\n" % player1Name
                )
                print(player1Choice)
                if player1Choice == "M" or player1Choice == "P":
                    break
                else:
                    print("illegal input, you have to enter the M or P")

        # CASE PLACE TOKEN
        if player1Choice == "P":
            x, y = getTokenCoordinates(board, player1Name)
            print("Here")
            # Create token
            token = Token(player1Name, player1.shape, x, y)
            # Place token and add to visited token list
            player1.placeToken(token)
            player1.addTokenToList(token)
            addToBoard(board, x, y, token.shape)
            print("Done1")


        # CASE MOVE TOKEN
        elif player1Choice == "M":
            while True:
                try:
                    stringInputCoordinate = input(
                        "\n%s, Please enter the coordinate of one of your placed tokens (EX: A2)\n" % player1Name)
                    # Parse string to numbers
                    convertedInputCoordinate = Methods.toRealCoordinates(stringInputCoordinate)
                    x = convertedInputCoordinate.x
                    y = convertedInputCoordinate.y
                    # check if the cell is not occupied and that the token doesn't belong to the other player
                    if (not isTheCellOccupied(board, x, y)) or (board[x][y] == player2.shape):
                        print("Please enter a valid token (one of your tokens)")

                    elif (isTheCellOccupied(board, x - 1, y + 1)) and (isTheCellOccupied(board, x, y + 1)) and (
                            isTheCellOccupied(board, x + 1, y + 1)) and (isTheCellOccupied(board, x - 1, y)) and (
                            isTheCellOccupied(board, x + 1, y)) and (isTheCellOccupied(board, x - 1, y - 1)) and (
                            isTheCellOccupied(board, x, y - 1)) and (isTheCellOccupied(board, x + 1, y - 1)):
                        print(
                            "Please choose a token that isn't surrounded by other tokens so that you may properly move it.")
                    else:
                        break
                except Exception as e:
                    print(
                        "Illegal input, you have to enter the alphabetic part (A to L) and numerical part (1 to 10 in )"
                        "order\nTry again.")

            selectedToken = Token(player1Name, player1.shape, x, y)
            while True:
                # try:
                direction = input(
                    "\n%s, Which way do you want to move?\nLEFT\nRIGHT\nUP\nDOWN\nUP-LEFT\nUP-RIGHT\nDOWN-LEFT\nDOWN-RIGHT\n"
                )
                print(direction)
                # Evaluates the move selected and checks its validity (if the cell is empty, or if it goes out of the board)
                attemptMove = evaluateMove(selectedToken, direction, player1, board)
                isValidMove = checkValidity(attemptMove, board)
                if isValidMove:
                    print("Move valid, moving token" + direction)
                    # selectedToken = attemptMove
                    break
                else:
                    print("Please select another move.")

            move(player1, player1.shape, attemptMove, selectedToken)
            removeFromBoard(board, selectedToken.coordinates.x, selectedToken.coordinates.y)
            addToBoard(board, attemptMove.coordinates.x, attemptMove.coordinates.y, player1.shape)

        # Player1 finish his turn
        printBoard(board)

        # Check player1 win or not
        if currentCounter >= 4:  # The 5th rounds
            if Methods.doIWin(player1, player2):
                print("\n%s, Congratulations!!! You win the game.\n" % player1Name)
                exit(0)

        # Print my tokenList
        for i in player1.tokenList:
            print(i.owner + ", You have placed token at X: " + str(i.coordinates.x) + " Y: " + str(
                i.coordinates.y) + "\n")

        ###########==================Player2==============########################
        # Player2 start to play
        player2Choice = ""
        if currentCounter == 0:
            player2Choice = "P"
        else:
            while True:  # this while loop is for determine the inputs valid or not
                player2Choice = input(
                    "\n%s, Please select what you want to do: \nMOVE(M) OR PLACE(P)\n" % player2Name
                )
                if player2Choice == "M" or player2Choice == "P":
                    break
                else:
                    print("illegal input, you have to enter the M or P")

        # CASE PLACE TOKEN
        if player2Choice == "P":
            x, y = getTokenCoordinates(board, player2Name)
            # Create token
            token = Token(player2Name, player2.shape, x, y)
            # Place token and add to visited token list
            player2.placeToken(token)
            player2.addTokenToList(token)
            addToBoard(board, x, y, token.shape)

        # CASE MOVE TOKEN
        elif player2Choice == "M":
            while True:
                try:
                    stringInputCoordinate = input(
                        "\n%s, Please enter the coordinate of one of your placed tokens (EX: A2)\n" % player2Name)
                    # Parse string to numbers
                    convertedInputCoordinate = Methods.toRealCoordinates(stringInputCoordinate)
                    x = convertedInputCoordinate.x
                    y = convertedInputCoordinate.y
                    # check if the cell is not occupied and that the token doesn't belong to the other player
                    if (not isTheCellOccupied(board, x, y)) or (board[x][y] == player1.shape):
                        print("Please enter a valid token (one of your tokens)")

                    elif (isTheCellOccupied(board, x - 1, y + 1)) and (isTheCellOccupied(board, x, y + 1)) and (
                            isTheCellOccupied(board, x + 1, y + 1)) and (isTheCellOccupied(board, x - 1, y)) and (
                            isTheCellOccupied(board, x + 1, y)) and (isTheCellOccupied(board, x - 1, y - 1)) and (
                            isTheCellOccupied(board, x, y - 1)) and (isTheCellOccupied(board, x + 1, y - 1)):
                        print(
                            "Please choose a token that isn't surrounded by other tokens so that you may properly move it.")
                    else:
                        break
                except Exception as e:
                    print(
                        "Illegal input, you have to enter the alphabetic part (A to L) and numerical part (1 to 10 in )"
                        "order\nTry again.")

            selectedToken = Token(player2Name, player2.shape, x, y)
            while True:
                try:
                    direction = input(
                        "\n%s, Which way do you want to move?\nLEFT\nRIGHT\nUP\n\DOWN\nUP-LEFT\nUP-RIGHT\nDOWN-LEFT\nDOWN-RIGHT"
                    )
                    # Evaluates the move selected and checks its validity (if the cell is empty, or if it goes out of the board)
                    attemptMove = evaluateMove(selectedToken, direction, player2, board)
                    isValidMove = checkValidity(attemptMove, board)
                    if isValidMove:
                        print("Move valid, moving token" + direction)
                        break
                    else:
                        print("Please select another move.")
                except Exception as e:
                    print(
                        "Illegal input, please enter one of the following:\nLEFT\nRIGHT\nUP\n\DOWN\nUP-LEFT\nUP-RIGHT\nDOWN-LEFT\nDOWN-RIGHT")

            # TODO: Add the coordinates and token inside the list.
            move(player2, player2.shape, attemptMove, selectedToken)
            removeFromBoard(board, selectedToken.coordinates.x, selectedToken.coordinates.y)
            addToBoard(board, attemptMove.coordinates.x, attemptMove.coordinates.y, player2.shape)

            # Player2 finish his turn
        printBoard(board)

        # Check player2 win or not
        if currentCounter >= 4:
            if Methods.doIWin(player2, player1):
                print("\n%s, Congratulations!!! You win the game.\n" % player2Name)
                exit(0)

        # After each turn, and counter will minus 1
        totalCounter = totalCounter - 1
        currentCounter = currentCounter + 1
    ###################################---Round End---#########################################################

    print("%s and %s. Thank you for playing X-Rudder Game, and there's no winner between yours.\n" % (
        player1Name, player2Name))


# For sprint 2
def startFightWithAIGameModel():
    print("Let's start fight with AI game model\n")

    board = [['_' for i in range(12)] for j in range(10)]
    print("Let's start two player game model\n")

    # Player1 setting
    player1Name = input("Player1\nPlease enter your name:\n")
    while not player1Name:
        player1Name = input("Invalid entry\nPlayer1\nPlease enter your name:\n")
    # Player1 default setting is X
    player1 = Player(player1Name, "X")

    # Player2 setting
    # Player2 default setting is O
    player2Name = "Computer"
    player2 = Player(player2Name, "O")
    print("Thank you, and let's start the game.\nThis is our initial empty board\n")

    ##############game start##################
    # Create a counter for maximum 30 turns
    totalCounter = 30
    currentCounter = 0
    # print current board
    printBoard(board)
    # initialize the coordinates
    x = 0
    y = 0
    while totalCounter > 0:
        print("\nRound " + str(currentCounter + 1))  # Print the current round

        # Player1 start to play
        x, y = getTokenCoordinates(board, player1Name)
        # Create token
        token = Token(player1Name, player1.shape, x, y)
        # Place token and add to visited token list
        player1.placeToken(token)
        player1.addTokenToList(token)
        addToBoard(board, x, y, token.shape)
        print(player1Name + ", placed token at X: " + str(x) + " Y: " + str(y) + "\n")
        # Player1 finish his turn
        printBoard(board)

        # Check player1 win or not
        if currentCounter >= 4:  # The 5th rounds
            if Methods.doIWin(player1, player2):
                print("\n%s, Congratulations!!! You win the game.\n" % player1Name)
                exit(0)

        # Print my tokenList
        # for i in player1.tokenList:
        #     print(i.owner + ", You have placed token at X: " + str(i.coordinates.x) + " Y: " + str(
        #         i.coordinates.y) + "\n")

        ###########==================Player2==============########################
        # Player2 start to play
        # x, y = getTokenCoordinates(board, player2Name)
        alpha = -2
        beta = 2
        depth = 0
        print('Computer is searching for a place...')
        start = time.time()
        (m, x, y, found, valueSet) = maximize(board, player1, player2, player2Name, player1Name, alpha, beta, depth)
        end = time.time()
        print('Evaluation time: {}s'.format(round(end - start, 7)))
        print("Heuristic value of node:" + str(m))
        print(player2Name + ", placed token at X: " + str(x) + " Y: " + str(y) + "\n")
        # Create token
        token = Token(player2Name, player2.shape, x, y)
        # Place token and add to visited token list
        player2.placeToken(token)
        player2.addTokenToList(token)
        addToBoard(board, x, y, token.shape)
        # Player2 finish his turn
        printBoard(board)

        # Check player2 win or not
        if currentCounter >= 4:
            if Methods.doIWin(player2, player1):
                print("\n%s, Congratulations!!! You win the game.\n" % player2Name)
                exit(0)

        # After each turn, and counter will minus 1
        totalCounter = totalCounter - 1
        currentCounter = currentCounter + 1
        ###################################---Round End---#########################################################

    print("%s and %s. Thank you for playing X-Rudder Game, and there's no winner between yours.\n" % (
        player1Name, player2Name))


# reference https://stackabuse.com/minimax-and-alpha-beta-pruning-in-python/
# Player 'O' is max, in this case AI
def maximize(board, player1, player2, player2Name, player1Name, alpha, beta, depth):
    maxv = -2
    px = None
    py = None
    depth = depth + 1
    # print(depth)

    maxWon = Methods.doIWin(player2, player1)
    minWon = Methods.doIWin(player1, player2)

    # variable to check if win for Ai(in this case max is ai) is found
    isfound = False
    # variable to check if x, y value is set the move which generated a win
    isvalueSet = False

    # if win for max is found
    if maxWon:
        # print("max - max won")
        isfound = True
        heuristicValue = depth
        return (heuristicValue, 0, 0, isfound, isvalueSet)

    if minWon:
        isfound = False
        heuristicValue = -1
        return (heuristicValue, 0, 0, isfound, isvalueSet)

    if depth == 27:
        heuristicValue = 1
        return (heuristicValue, 0, 0, isfound, isvalueSet)

    for i in range(0, 10):
        # check if a filed on board is empty is so then place a token for the player
        for j in range(0, 12):
            if board[i][j] == '_':
                # On the empty field player 'O' makes a move and calls Min
                # That's one branch of the game tree.
                # placing a temporary token for the player to generate a board to check for moves
                token = Token(player2Name, player2.shape, i, j)
                # Place token and add to visited token list
                player2.placeToken(token)
                player2.addTokenToList(token)
                addToBoard(board, i, j, token.shape)
                # print("maximize: " + player2.shape)
                # printBoard(board)
                (m, min_i, min_j, found, valueSet) = minimize(board, player1, player2, player2Name, player1Name, alpha,
                                                              beta, depth)
                depth = m
                isfound = found
                isvalueSet = valueSet

                if m > maxv and not isvalueSet:
                    # print("in m > max-> m: " + str(m) + " maxv: " + str(maxv))
                    maxv = m
                    px = i
                    py = j
                    # print("in m > max-> m: " + str(m) + " maxv: " + str(maxv) + " i: " + str(i) + " j: " + str(j))
                # Setting back the field to empty
                # removing the temporary token that was added to board to bring board to initial configuration
                player2.removeTokenCoordinates(token)
                player2.removeFromTokenList(token)
                board[i][j] = '_'
                # printBoard(board)

                if maxv >= beta:
                    # print("in  maxv >= beta: ->  maxv: " + str(maxv) + " i: " + str(px) + " j: " + str(py))
                    return (maxv, px, py, isfound, isvalueSet)

                if maxv > alpha:
                    alpha = maxv

                    # checking if win was found but the value is not yet set - setting value and returning x,y for winning move
                if isfound and not isvalueSet:
                    px = i
                    py = j
                    isvalueSet = True
                    # print(str(i) + " MAX " + str(j))
                    return (maxv, px, py, isfound, isvalueSet)

                    # if the value x, y is already set then return that same value which generated win from function call
                if valueSet:
                    return (m, min_i, min_j, isfound, isvalueSet)

    return (maxv, px, py, isfound, isvalueSet)


# Player 'X' is min, in this case human
def minimize(board, player1, player2, player2Name, player1Name, alpha, beta, depth):
    minv = 2
    qx = None
    qy = None
    depth = depth + 1
    # print(depth)

    maxWon = Methods.doIWin(player2, player1)
    minWon = Methods.doIWin(player1, player2)
    # variable to check if win for Ai(in this case max is ai) is found
    isfound = False
    # variable to check if x, y value is set the move which generated a win
    isvalueSet = False

    # if win for max is found
    if maxWon:
        # print("min - max won")
        isfound = True
        heuristicValue = depth
        return (heuristicValue, 0, 0, isfound, isvalueSet)

    if minWon:
        isfound = False
        heuristicValue = -1
        return (heuristicValue, 0, 0, isfound, isvalueSet)

    if depth == 27:
        heuristicValue = 1
        return (heuristicValue, 0, 0, isfound, isvalueSet)

    for i in range(0, 10):
        # check if a filed on board is empty is so then place a token for the player
        for j in range(0, 12):
            # check if a filed on board is empty is so then place a token for the player
            if board[i][j] == '_':
                # placing a temporary token for the player to generate a board to check for moves
                token = Token(player1Name, player1.shape, i, j)
                # Place token and add to visited token list
                player1.placeToken(token)
                player1.addTokenToList(token)
                addToBoard(board, i, j, token.shape)
                # print("minimize: " + player1.shape)
                # printBoard(board)
                (m, max_i, max_j, found, valueSet) = maximize(board, player1, player2, player2Name, player1Name, alpha,
                                                              beta, depth)
                depth = m
                isfound = found
                isvalueSet = valueSet

                if m < minv:
                    minv = m
                    qx = i
                    qy = j
                # removing the temporary token that was added to board to bring board to initial configuration
                player1.removeTokenCoordinates(token)
                player1.removeFromTokenList(token)
                board[i][j] = '_'

                if minv <= alpha:
                    # print("in  minv <= alpha:: ->  minv: " + str(minv) + " i: " + str(qx) + " j: " + str(qy))
                    return (minv, qx, qy, isfound, isvalueSet)

                if minv < beta:
                    beta = minv

                    # checking if win was found but the value is not yet set - setting value and returning x,y for winning move
                if isfound and not isvalueSet:
                    isvalueSet = True
                    # print(str(i) + " MIN " + str(j))
                    return (m, max_i, max_j, isfound, isvalueSet)

                    # if the value x, y is already set then return that same value which generated win from function call
                if isvalueSet:
                    return (m, max_i, max_j, isfound, isvalueSet)

    return (minv, qx, qy, isfound, isvalueSet)
