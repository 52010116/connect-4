
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