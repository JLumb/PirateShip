import random
import time
 
# Variables for the player and computer game board

PLAYER_BOARD = [[" "] * 10 for i in range(10)]
COMPUTER_BOARD = [[" "] * 10 for i in range(10)]
PLAYER_GUESS_BOARD = [[" "] * 10 for i in range(10)]
COMPUTER_GUESS_BOARD = [[" "] * 10 for i in range(10)]

# Converting strings into integers
LETTER_TRANSLATE = {"A": 0, "B": 1, "C": 2, "D": 3, "E": 4, "F": 5, "G": 6, "H": 7}

# Seperator creates a line break
SEPERATOR = "~" * 80

# The opening message that a user will see when PirateShips runs
print(SEPERATOR)

def welcome_message(): 
    print("\033[1;32;40m Ahoy Matey, welcome to PirateShips defeat your enemies")
    print("\033[1;32;40m and make way with the treasures!")
    print("\033[1;32;40m The high sea's have but a few rules:")













welcome_message()