import random
import time

PLAYER_BOARD = [[" "]] * 10 for i in range(10)]
COMPUTER_BOARD = [[" "]] * 10 for i in range(10)]
PLAYER_GUESS = [[" "]] * 10 for i in range(10)]
COMPUTER_GUESS = [[" "]] * 10 for i in range(10)]

LETTER_TRANSLATE = {"A": 0, "B": 1, "C": 2, "D": 3, "E": 4, "F": 5, "G": 6, "H": 7}