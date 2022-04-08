
class Field:

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
            print("Sorry, the column is already full")
            return True