import random
import time
 
 
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
    print("\033[1;32;48mAHOY MATEY, WELCOME TO PIRATESHIPS DEFEAT YOUR ENEMIES")
    print("\033[1;32;48mAND PLUNDER ALL THE TREASURES!\n")
    print("""\033[1;31;48mThe aim of the game is to destroy the enemy fleet,
before they destroy yours. The winner takes away endless treasure
and more importantly their name will become legend\n""")

    print("\033[1;32;48mTHE HIGH SEA'S HAVE BUT A FEW RULES:\n")
    print("\033[1;31;48mRule #1: Show no mercy to the fools that challenge you!")
    print("\033[1;31;48mRule #2: All ships must be placed on the board")
    print("\033[1;31;48mRule #3: The first to destroy the enemy ships wins\n")
    print(SEPERATOR)

    print("\033[1;32;48mHOW TO PLAY:\n")
    print("\033[1;31;48mPirateShips is a turn based game vs AI:")
    print("\033[1;31;48mYou will pick a co-ordinate on the game board example: A1.")
    print("\033[1;31;48mYou will then see a message of hit or miss.")
    print("\033[1;31;48mThe first to blow all the enemy ships out of the water wins.\n")

def username_input():
    """Takes user input to create a username as a variable that can be used
    throughout the app"""
    print("\033[1;32;48mWHO IS IT THAT DARES ENTER THESE TREACHEROUS SEAS?\n")
    while True:
        username = input("\033[1;32;48mENTER YUR NAME CPT'N: ")
        if verify_username(username):
            break
    print(f"\033[1;31;48mCPT'N {username} WILL STRIKE FEAR INTO THE HEART OF THEIR FOES")

def verify_username(username):
    """
    Verifies that the username is within the guidelines of the game
    """
    if len(username) > 8:
        print("INVALID USER, 8 CHARACTERS MAXIMUM")
        return False       
    elif len(username) == 0:
        print("NO USERNAME ENTERED PLEASE RETRY")
        return False
    else:
        return True


def print_board(board):
    """
    this function prints the game board out throughtout the project
    """
    print("A B C D E F G H")
    print("~ ~ ~ ~ ~ ~ ~ ~")
    row_number = 1
    for row in board:
        print("%d|%s" % (row_number, "|".join(row)))
        row_number += 1








welcome_message()
username_input()