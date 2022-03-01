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
SEPERATOR = "\033[1;35;48m~" * 80

# The opening message that a user will see when PirateShips runs


def welcome_message():
    """
    The welcome message and rules that will be the first thing the user will
    see when PirateShips runs
    """
    print(SEPERATOR)
    print("\033[1;32;48mAhoy Matey, welcome to PirateShips defeat your enemies")
    print("\033[1;32;48mand make way with the treasures!\n")
    print("""\033[1;31;48mThe aim of the game is to destroy the enemy fleet,
before they destroy yours. The winner takes away endless treasure
and more importantly their name will become legend\n""")

    print("\033[1;32;48mThe high sea's have but a few rules:\n")
    print("\033[1;31;48mRule #1: Have no mercy on the enemy")
    print("\033[1;31;48mRule #2: All ships must be placed within the board")
    print("\033[1;31;48mRule #3: The first to hit the enemy ships 15 times wins\n")
    print(SEPERATOR)
    














welcome_message()