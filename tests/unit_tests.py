import unittest
from game.game import *


class MyTestCase(unittest.TestCase):

    def test_field_init(self):
        test_field = Field()
        expected = [
            ["_", "_", "_", "_", "_", "_", "_"],
            ["_", "_", "_", "_", "_", "_", "_"],
            ["_", "_", "_", "_", "_", "_", "_"],
            ["_", "_", "_", "_", "_", "_", "_"],
            ["_", "_", "_", "_", "_", "_", "_"],
            ["_", "_", "_", "_", "_", "_", "_"],
        ]
        self.assertEqual(test_field.current_state(), expected)

    def test_exit_input(self):
        test_field = Field()
        input_uppercase = "Q"
        input_lowercase = "q"
        input_str_wrong = "k"
        input_int_wrong = 1

        self.assertEqual(test_field.exit_game(input_uppercase), True)
        self.assertEqual(test_field.exit_game(input_lowercase), True)
        self.assertEqual(test_field.exit_game(input_str_wrong), False)
        self.assertEqual(test_field.exit_game(input_int_wrong), False)

    def test_legal_move_check(self):

        test_field = Field()

        # checks if input was int
        input_str = "g"
        input_str_2 = "K"
        self.assertEqual(test_field.check_legal_move(input_str), True)
        self.assertEqual(test_field.check_legal_move(input_str_2), True)

        # checks if input is out of range
        input_to_small = -5
        input_to_small_2 = -1
        input_to_large = 8
        input_to_large_2 = 7
        self.assertEqual(test_field.check_legal_move(input_to_small), True)
        self.assertEqual(test_field.check_legal_move(input_to_small_2), True)
        self.assertEqual(test_field.check_legal_move(input_to_large), True)
        self.assertEqual(test_field.check_legal_move(input_to_large_2), True)

    def test_set_move(self):
        test_field1 = Field()

        test_field1.set_move(0, "X")
        exp = [
            ["_", "_", "_", "_", "_", "_", "_"],
            ["_", "_", "_", "_", "_", "_", "_"],
            ["_", "_", "_", "_", "_", "_", "_"],
            ["_", "_", "_", "_", "_", "_", "_"],
            ["_", "_", "_", "_", "_", "_", "_"],
            ["X", "_", "_", "_", "_", "_", "_"],
        ]
        self.assertEqual(test_field1.current_state(), exp)

        test_field2 = Field()
        test_field2.set_move(6, "P")
        expected = [
            ["_", "_", "_", "_", "_", "_", "_"],
            ["_", "_", "_", "_", "_", "_", "_"],
            ["_", "_", "_", "_", "_", "_", "_"],
            ["_", "_", "_", "_", "_", "_", "_"],
            ["_", "_", "_", "_", "_", "_", "_"],
            ["_", "_", "_", "_", "_", "_", "P"],
        ]
        self.assertEqual(test_field2.current_state(), expected)

        test_field3 = Field()

        test_field3.set_move(6, "P")
        test_field3.set_move(6, "X")
        expected = [
            ["_", "_", "_", "_", "_", "_", "_"],
            ["_", "_", "_", "_", "_", "_", "_"],
            ["_", "_", "_", "_", "_", "_", "_"],
            ["_", "_", "_", "_", "_", "_", "_"],
            ["_", "_", "_", "_", "_", "_", "X"],
            ["_", "_", "_", "_", "_", "_", "P"],
        ]
        self.assertEqual(test_field3.current_state(), expected)

    def test_legal_move_check2(self):
        test_field4 = Field()
        self.assertEqual(test_field4.check_legal_move(0), False)

        for i in range(6):
            test_field4.set_move(0, "X")

        x = (test_field4.current_state())
        expected_field1 = [
            ["X", "_", "_", "_", "_", "_", "_"],
            ["X", "_", "_", "_", "_", "_", "_"],
            ["X", "_", "_", "_", "_", "_", "_"],
            ["X", "_", "_", "_", "_", "_", "_"],
            ["X", "_", "_", "_", "_", "_", "_"],
            ["X", "_", "_", "_", "_", "_", "_"],
        ]
        self.assertEqual(x, expected_field1)
        self.assertEqual(test_field4.check_legal_move(0), True)

    def test_check_if_win(self):
        # vertical
        field5 = Field()
        for i in range(4):
            field5.set_move(0,"X")

        self.assertEqual(field5.check_win("X"), True)

        # horizontal
        field6 = Field()
        for i in range(4):
            field6.set_move(i, "X")

        self.assertEqual(field6.check_win("X"), True)

        # diagonal /
        field7 = Field()
        field7.set_move(0, "X")
        field7.set_move(1, "P")
        field7.set_move(1, "X")
        field7.set_move(2, "P")
        field7.set_move(2, "X")
        field7.set_move(2, "X")
        field7.set_move(3, "P")
        field7.set_move(3, "X")
        field7.set_move(3, "P")
        field7.set_move(3, "X")

        self.assertEqual(field7.check_win("X"), True)

        # diagonal \
        field8 = Field()
        field8.set_move(6, "X")
        field8.set_move(5, "P")
        field8.set_move(5, "X")
        field8.set_move(4, "P")
        field8.set_move(4, "X")
        field8.set_move(4, "X")
        field8.set_move(3, "P")
        field8.set_move(3, "X")
        field8.set_move(3, "P")
        field8.set_move(3, "X")

        self.assertEqual(field8.check_win("X"), True)


if __name__ == '__main__':
    unittest.main()