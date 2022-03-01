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
SEPERATOR = "\033[1;35;40m~" * 80

# The opening message that a user will see when PirateShips runs


def welcome_message():
    """
    The welcome message and rules that will be the first thing the user will
    see when PirateShips runs
    """
    print(SEPERATOR)
    print("\033[1;32;40m Ahoy Matey, welcome to PirateShips defeat your enemies")
    print("\033[1;32;40m and make way with the treasures!\n")
    print("""\033[1;31;40m The aim of the game is to destroy the enemy fleet,
 before they destroy yours. The winner takes away endless treasure
 and more importantly their name will become legend\n""")

    print("\033[1;32;40m The high sea's have but a few rules:\n")
    print("\033[1;31;40m Rule #1: Have no mercy on the enemy")
    print("\033[1;31;40m Rule #2: All ships must be placed within the board")
    print("\033[1;31;40m Rule #3: The first to hit the enemy ships 15 times wins\n")
    print(SEPERATOR)













welcome_message()