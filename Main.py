# This it the main class start to play the game
import MainMethods

print("Welcome To X-Rudder Game.\n"
      "Choose your game mode\n"
      "1. Two player modes\n"
      "2. Fight with AI\n"
      "3. Exit game\n")
number = input("Enter your choice: ")
while True:
    if str(number) == '1':
        print("You choice two player game mode\n")
        MainMethods.startTwoPlayerGame()
        break
    elif str(number) == '2':
        print("You choice fight with AI game mode\n")
        MainMethods.startFightWithAIGameModel()
        break
    elif str(number) == '3':
        print("Game Exit!!!\n")
        exit(0)
    else:
        number = input("You choose wrong choice, please enter it again.\nEnter your choice: ")

