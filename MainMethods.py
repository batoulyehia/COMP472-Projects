from Player import *
import string


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
    newCoordinates = newToken.getCoordinates()  # remove that token from the list
    print("newCoordinates" + str(newCoordinates))
    # player.tokenList.remove(oldToken)      #create new token based on these coordinates

    # getVisitedCoordinatesFromPlayer = player.visitedCoordinates
    # getVisitedCoordinatesFromPlayer.remove(oldCoordinates) #removes old coordinates
    # newToken = Token(player, shape, newCoordinates.x, newCoordinates.y) #creates new Token
    # player.placeToken(newToken) #inserts the token inside of the visited coordinates list
    # gettokenListFromPlayer = player.tokenList
    # gettokenListFromPlayer.append(newToken) #places token inside the token list

    x1 = oldToken.coordinates.x
    y1 = oldToken.coordinates.y
    oldCoordinates = Coordinates(x1, y1)
    print(oldCoordinates.x)
    print(oldCoordinates.y)

    # player.removeTokenCoordinates(oldCoordinates)
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

    player1Name = input("Player1\nPlease enter your name:\n")
    while not player1Name:
        player1Name = input("Invalid entry\nPlayer1\nPlease enter your name:\n")
    # Player1 default setting is X
    player1 = Player(player1Name, "X")
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
        print("\nRound " + str(currentCounter + 1))
        # Player1 start to play
        player1Choice = ""
        if currentCounter == 0:
            player1Choice = "PLACE"
        else:
            player1Choice = input(
                "\n%s, Please select what you want to do: \nMOVE\nPLACE"
            )

        while player1Choice != "PLACE" or player1Choice != "MOVE":
            # CASE PLACE TOKEN
            if player1Choice == "PLACE":
                while True:
                    try:
                        stringCoordinate = input(
                            "\n%s, Please enter your coordinate and place your token (EX : A2)\n" % player1Name)
                        # Parse string to numbers
                        numberCoordinate = Methods.toRealCoordinates(stringCoordinate)
                        # Get coordinate x and y
                        x = numberCoordinate.x
                        y = numberCoordinate.y
                        # Check if the cell occupied
                        if isTheCellOccupied(board, x, y):
                            print("The cell is already occupied, please enter another coordinates")
                        else:
                            break
                    except Exception as e:
                        print(
                            "illegal input, you have to enter the alphabetic part (A to L) and numerical part (1 to 10) in "
                            "order\nTry again")
                # Create token
                token = Token(player1Name, player1.shape, x, y)
                # Place token and add to visited token list
                player1.placeToken(token)
                player1.addTokenToList(token)
                addToBoard(board, x, y, token.shape)
                break

            # CASE MOVE TOKEN
            elif player1Choice == "MOVE":
                while True:
                    try:
                        stringInputCoordinate = input(
                            "\n%s, Please enter the coordinate of one of your placed tokens (EX: A2)\n" % player1Name)
                        # Parse string to numbers
                        convertedInputCoordinate = Methods.toRealCoordinates(stringInputCoordinate)
                        x = convertedInputCoordinate.x
                        y = convertedInputCoordinate.y
                        # check if the cell is not occupied and that the token doesn't belong to the other player
                        if (board[x][y] == '_') or (board[x][y] == player2.shape):
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
                        "\n%s, Which way do you want to move?\nLEFT\nRIGHT\nUP\n\DOWN\nUP-LEFT\nUP-RIGHT\nDOWN-LEFT\nDOWN-RIGHT"
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
                # except Exception as e:
                #     print("Illegal input, please enter one of the following:\nLEFT\nRIGHT\nUP\n\DOWN\nUP-LEFT\nUP-RIGHT\nDOWN-LEFT\nDOWN-RIGHT")
                #
                # TODO: Add the coordinates and token inside the list.
                move(player1, player1.shape, attemptMove, selectedToken)
                removeFromBoard(board, selectedToken.coordinates.x, selectedToken.coordinates.y)
                addToBoard(board, attemptMove.coordinates.x, attemptMove.coordinates.y, player1.shape)
                break

            else:
                print("Please select either MOVE or PLACE")

                # Player1 finish his turn
        printBoard(board)

        # Check player1 win or not
        if currentCounter >= 4:
            if Methods.doIWin(player1, player2):
                print("\n%s, Congratulations!!! You win the game.\n" % player1Name)
                exit(0)

        player1Choice = ""
        for i in player1.tokenList:
            print(i.owner)
            print(i.shape)
            print(i.coordinates.x)

        ###########================================########################
        # Player2 start to play
        player2Choice = ""
        if currentCounter == 0:
            player2Choice = "PLACE"
        else:
            player2Choice = input(
                "\n%s, Please select what you want to do: \nMOVE\nPLACE"
            )

        while player2Choice != "PLACE" or player2Choice != "MOVE":
            # CASE PLACE TOKEN
            if player2Choice == "PLACE":
                while True:
                    try:
                        stringCoordinate = input(
                            "\n%s, Please enter your coordinate and place your token (EX : A2)\n" % player2Name)
                        # Parse string to numbers
                        numberCoordinate = Methods.toRealCoordinates(stringCoordinate)
                        # Get coordinate x and y
                        x = numberCoordinate.x
                        y = numberCoordinate.y
                        # Check if the cell occupied
                        if isTheCellOccupied(board, x, y):
                            print("The cell is already occupied, please enter another coordinates")
                        else:
                            break
                    except Exception as e:
                        print(
                            "illegal input, you have to enter the alphabetic part (A to L) and numerical part (1 to 10) in "
                            "order\nTry again")
                # Create token
                token = Token(player2Name, player2.shape, x, y)
                # Place token and add to visited token list
                player2.placeToken(token)
                player2.addTokenToList(token)
                addToBoard(board, x, y, token.shape)
                break

            # CASE MOVE TOKEN
            elif player2Choice == "MOVE":
                while True:
                    try:
                        stringInputCoordinate = input(
                            "\n%s, Please enter the coordinate of one of your placed tokens (EX: A2)\n" % player2Name)
                        # Parse string to numbers
                        convertedInputCoordinate = Methods.toRealCoordinates(stringInputCoordinate)
                        x = convertedInputCoordinate.x
                        y = convertedInputCoordinate.y
                        # check if the cell is not occupied and that the token doesn't belong to the other player
                        if (board[x][y] == '_') or (board[x][y] == player1.shape):
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
                        attemptMove = evaluateMove(selectedToken, direction, player2,board)
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
                break

            else:
                print("Please select either MOVE or PLACE")

                # Player2 finish his turn
        printBoard(board)

        # Check player1 win or not
        if currentCounter >= 4:
            if Methods.doIWin(player2, player1):
                print("\n%s, Congratulations!!! You win the game.\n" % player1Name)
                exit(0)

        player2Choice = ""

        # After each turn, and counter will minus 1
        totalCounter = totalCounter - 1
        currentCounter = currentCounter + 1

    print("%s and %s. Thank you for playing X-Rudder Game, and there's no winner between yours.\n" % (
        player1Name, player2Name))


# For sprint 2
def startFightWithAIGameModel():
    print("Let's start fight with AI game model\n")

# For testing
# alphabet = list(string.ascii_uppercase[0:12])
# board = [['_' for i in range(12)] for j in range(10)]
# for cell in alphabet:
#     print(cell, end=" ")
# print()
# printBoard(board)
