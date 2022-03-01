import random
import time
 
# Variables for the player and computer game board
PLAYER_BOARD = [[" "]] * 10 for i in range(10)]
COMPUTER_BOARD = [[" "]] * 10 for i in range(10)]
PLAYER_GUESS = [[" "]] * 10 for i in range(10)]
COMPUTER_GUESS = [[" "]] * 10 for i in range(10)]

# Converting strings into integers
LETTER_TRANSLATE = {"A": 0, "B": 1, "C": 2, "D": 3, "E": 4, "F": 5, "G": 6, "H": 7}

# Seperator creates a line break
SEPERATOR = "~" * 80

# The opening message that a user will see when PirateShips runs
def welcome_message():
    """
    Ahoy Matey, welcome to PirateShips defeat your enemies
    make away with the treasures!
    """













welcome_message()