import random
import time
 
# Variables for the player and computer game board

PLAYER_BOARD = [[" "] * 8 for i in range(8)]
COMPUTER_BOARD = [[" "] * 8 for i in range(8)]
PLAYER_GUESS_BOARD = [[" "] * 8 for i in range(8)]
COMPUTER_GUESS_BOARD = [[" "] * 8 for i in range(8)]

# Converting strings into integers
LETTER_TRANSLATE = {"A": 0, "B": 1, "C": 2, "D": 3, "E": 4, "F": 5, "G": 6, "H": 7}

# Seperator creates a line break
SEPERATOR = "~" * 80

# The opening message that a user will see when PirateShips runs
def welcome_message():
    print("Ahoy Matey, welcome to PirateShips defeat your enemies make way with the treasures!")
    print('\x1b[6;30;42m' + 'Success!' + '\x1b[0m')












welcome_message()