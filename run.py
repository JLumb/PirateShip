import random

# Seperator creates a line break
SEPERATOR = "\033[1;35;48m~" * 80


# The opening message that a user will see when PirateShips runs


def welcome_message():
    """
    The welcome message and rules that will be the first thing the user will
    see when PirateShips runs
    """
    print(SEPERATOR)
    print("\033[1;32;48mAHOY MATEY, WELCOME TO PIRATESHIP DEFEAT YOUR ENEMIES")
    print("\033[1;32;48mAND PLUNDER ALL THE TREASURES!\n")
    print("""\033[1;31;48mThe aim of the game is to destroy the enemy fleet""")

    print("\033[1;32;48mTHE HIGH SEA'S HAVE BUT A FEW RULES:\n")
    print("\033[1;31;48mRule #1: Show no mercy to the fools that challenge you!")
    print("""\033[1;31;48mRule #2: Destroy all enemy ships
before you run out of cannonballs! \n""")
    print(SEPERATOR)

    print("\033[1;32;48mHOW TO PLAY:\n")
    print("\033[1;31;48mYou will pick a co-ordinate on the game board example: A1.")
    print("""\033[1;31;48mYou will then see a message of hit or miss,
on the board a x will show for hit and a ~ for miss!.""")
    print("""\033[1;31;48mBlow up all enemy ship
before running out of cannonballs to win.\n""")


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


class PlayBoard:
    """
    Class to initiate the game board
    """
    def __init__(self, board):
        self.board = board

    def letter_converter(self):
        """converts the strings into integers so that the computer can read"""
        convert = {"A": 0, "B": 1, "C": 2, "D": 3, "E": 4, "F": 5, "G": 6, "H": 7}
        return convert

    def print_board(self):
        """
        this function prints the game board out throughtout the project
        """
        print("  A B C D E F G H")
        print("  ~ ~ ~ ~ ~ ~ ~ ~")
        row_number = 1
        for row in self.board:
            print("%d|%s" % (row_number, "|".join(row)))
            row_number += 1


class Pirateship:

    """class to take user input and run the pirateship game functions"""
    def __init__(self, board):
        self.board = board

    def user_guess(self):
        """takes the users guess and checks to see if it is a valid input"""
        try:
            x_row = input("Enter the Row:")
            while x_row not in "123456":
                print("Please enter number between 1 and 6")
                x_row = input("Enter the Row: ")

            y_column = input("Enter the Column: ").upper()
            while y_column not in "ABCDEFGH":
                print("Please enter a value from ABCDEFGH")
                y_column = input("Enter the Column:")
            return int(x_row) - 1, PlayBoard.letter_converter(self)[y_column]
        except ValueError:
            print("Not a valid input")
            return self.user_guess()

    def players_ships(self):
        """creating the ships for the board and
        checking if space taken when placing"""
        for ship in range(7):
            self.x_row, self.y_column = random.randint(0, 5), random.randint(0, 5)
            while self.board[self.x_row][self.y_column] == "X":
                self.x_row, self.y_column = random.randint(0, 5), random.randint(0, 5)
            self.board[self.x_row][self.y_column] = "X"
        return self.board

    def hit_count(self):
        """counts the amount of ships hit so we can
        calculate when to game is over"""
        hit_ships = 0
        for row in self.board:
            for column in row:
                if column == "X":
                    hit_ships += 1
        return hit_ships


def start_game():
    """this function will be called to start and
        run the game of PirateShips this includes
        counting turns left(cannonballs remaining)"""

    computer_board = PlayBoard([[" "] * 8 for i in range(6)])
    guess_board = PlayBoard([[" "] * 8 for i in range(6)])
    Pirateship.players_ships(computer_board)
    cannon_balls_left = 25
    while cannon_balls_left > 0:
        PlayBoard.print_board(guess_board)

        user_row, user_column = Pirateship.user_guess(object)

        while guess_board.board[user_row][user_column] == "~" or guess_board.board[user_row][user_column] == "X":
            print("\033[1;35;48mYou have already hit that location, Try again.")
            x_row, y_column = Pirateship.user_guess(object)
            break

        if computer_board.board[user_row][user_column] == "X":
            print("\033[1;32;48mYou sunk one of their ships, keep going!")
            guess_board.board[user_row][user_column] = "X"
        else:
            print("\033[1;35;48mThat is a miss!")
            guess_board.board[user_row][user_column] = "~"

        if Pirateship.hit_count(guess_board) == 7:
            guess_board.board[user_row][user_column] = "X"
            print("""\033[1;32;48mThat was the last ship CAPT'N! take the loot and
dissappear into the high sea's""")
            break
        else:
            cannon_balls_left -= 1
            print(f"\033[1;35;48mBE AWARE CAP, ONLY {cannon_balls_left} CANNONBALLS LEFT.")
        if cannon_balls_left == 0:
            print("\033[1;31;48mOUT OF CANNONBALLS CAPT'N WE MUST RETREAT!!!")
            break

def play_again():

    """
    asks the player if they would like to play again
    """
    print("Give it another go CAPT'N? \n")
    answer = input("ENTER YAY OR NEIGH: \n").upper()
    print(' ')
    while True:
        if answer == "YAY":
            print(SEPERATOR)
            welcome_message()
        elif answer == "NEIGH":
            print('SEE YOU AGAIN SOON CAP')
            print(SEPERATOR)
            return False
        else:
            print(' ')
            print('PLEASE ENTER YAY OR NEIGH')
            answer = input('ENTER YAY OR NEIGH: \n').upper()


welcome_message()
username_input()
start_game()
play_again()
