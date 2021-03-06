from random import randint
import numpy as np
from os import system, name


class Field:
    """creates and prints playingfield
    exits game if input is Q/q
    checks if move is legal or not
    checks if someone has won
    """

    def __init__(self):
        self.board = [
            ["_", "_", "_", "_", "_", "_", "_"],
            ["_", "_", "_", "_", "_", "_", "_"],
            ["_", "_", "_", "_", "_", "_", "_"],
            ["_", "_", "_", "_", "_", "_", "_"],
            ["_", "_", "_", "_", "_", "_", "_"],
            ["_", "_", "_", "_", "_", "_", "_"],
        ]
        self.column = 7
        self.row = 6

    def current_state(self):
        return self.board

    def exit_game(self, input):
        if input == "q" or input == "Q":
            return True
        else:
            return False

    def check_legal_move(self, input):
        if not isinstance(input, int):
            print("Wrong type of input")
            return True

        if 0 > input:
            print("Your input is to small!")
            return True

        if input > 6:
            print("Your input is to large!")
            return True

        if self.board[0][input] == "_":
            return False
        else:
            print("Sorry, the column is already full, please choose a different one!")
            return True

    def set_move(self, X, Symbol):
        """ The function “set_move” puts Playersymbol into the chosen spot"""

        for i in range(5, -1, -1):
            if self.board[i][X] == "_":
                self.board[i][X] = Symbol
                break
            else:
                continue

    def check_win(self, Symbol):
        """Every Round the Field gets checked for a winner. Horizontally, Certically
        and Diagonally (twice for both possibilities)"""

        for x in range(self.column - 3):
            for y in range(self.row):
                if self.board[y][x] == Symbol and self.board[y][x + 1] == Symbol and self.board[y][x + 2] == Symbol and \
                        self.board[y][x + 3] == Symbol:
                    return True

        for x in range(self.column):
            for y in range(self.row - 3):
                if self.board[y][x] == Symbol and self.board[y + 1][x] == Symbol and self.board[y + 2][x] == Symbol and \
                        self.board[y + 3][x] == Symbol:
                    return True

        for x in range(self.column - 3):
            for y in range(self.row - 3):
                if self.board[y][x] == Symbol and self.board[y + 1][x + 1] == Symbol and self.board[y + 2][x + 2] == \
                        Symbol and self.board[y + 3][x + 3] == Symbol:
                    return True

        for x in range(self.column - 3):
            for y in range(3, self.row):
                if self.board[y][x] == Symbol and self.board[y - 1][x + 1] == Symbol and self.board[y - 2][x + 2] == \
                        Symbol and self.board[y - 3][x + 3] == Symbol:
                    return True

    def print_field(self):
        for row in self.board:
            for i in row:
                print(f"{i} ", end="")
            print()
        num = ["0", "1", "2", "3", "4", "5", "6"]
        print(' '.join(num))
        print("")


if __name__ == "__main__":

    field = Field()


    def ai_move(field):
        """Very basic AI with randint that a player can choose to play against"""
        while True:

            col = randint(0, 6)
            if not field.check_legal_move(col):
                field.set_move(col, "A")
                if field.check_win("A"):
                    field.print_field()
                    print("AI Won")
                    quit()
                break
            else:
                continue


    while True:
        """asks player if he wants to play against AI or a Human"""
        try:
            p = int(input("Welcome to the game, do you want to play against AI (1) or another Player (2)? "))
        except ValueError:
            print("Please enter an Integer!")
            continue
        if p not in [1, 2] or not isinstance(p, int):
            print("Please enter 1 or 2 as Integer!")
            continue
        else:
            break

    if p == 1:
        """Player chose AI Game and gets another chance to quit the game, otherwise the game continues until 
        someone won"""
        print("AI-Game, if you want to exit the game enter q! ")
        while True:
            field.print_field()
            inp = input("Which column? ")
            if isinstance(inp, str):
                if field.exit_game(inp):
                    print("Game is terminated!")
                    quit()
            try:
                input_up = int(inp)
            except ValueError:
                print("Please enter q to quit or ent an Integer ")
                continue
            if field.check_legal_move(input_up):
                continue
            field.set_move(input_up, "X")
            if field.check_win("X"):
                field.print_field()
                print("Player won!")
                quit()
            ai_move(field)

    if p == 2:
        """Player chose PvP mode and gets another chance to quit the game otherwise the game continues until 
        someone won"""
        print("Player(X) vs Player(P), if you want to exit the game enter q! ")
        while True:
            # Player One (X)
            while True:
                field.print_field()
                inp = input("Player X choose a column: ")
                if isinstance(inp, str):
                    if field.exit_game(inp):
                        print("Game is terminated")
                        quit()
                try:
                    input_up = int(inp)
                except ValueError:
                    print("please enter 'q' to quit or an Integer ")
                    continue
                if field.check_legal_move(input_up):
                    continue
                field.set_move(input_up, "X")
                if field.check_win("X"):
                    field.print_field()
                    print("Player X won")
                    quit()
                break

            # Player Two (P)
            while True:
                field.print_field()
                inp = input("Player P choose a column: ")
                if isinstance(inp, str):
                    if field.exit_game(inp):
                        print("Game is terminated")
                        quit()
                try:
                    input_up = int(inp)
                except ValueError:
                    print("please enter 'q' to quit or an Integer")
                    continue
                if field.check_legal_move(input_up):
                    continue
                field.set_move(input_up, "P")
                if field.check_win("P"):
                    field.print_field()
                    print("Player P won")
                    quit()
                break

"""For playing again you need to restart the game"""
