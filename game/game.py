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

    def set_move(self, X, Symbol):

        for i in range(5, -1, -1):
            if self.board[i][X] == "_":
                self.board[i][X] = Symbol
                break
            else:
                continue

    def check_win(self, Symbol):

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

    def print_field(self):
        for row in self.board:
            for i in row:
                print(f"{i} ", end="")
            print()
        num = ["0", "1", "2", "3", "4", "5", "6"]
        print(' '.join(num))
        print("")
