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
        self.assertEqual(test_field.check_legal_move(input_str), True)

        # checks if input is out of range
        input_to_small = -5
        input_to_large = 8
        self.assertEqual(test_field.check_legal_move(input_to_small), True)
        self.assertEqual(test_field.check_legal_move(input_to_large), True)

    def test_set_move(self):
        test_field1 = Field()

        test_field1.set_move(0,"X")
        expected =[
            ["_", "_", "_", "_", "_", "_", "_"],
            ["_", "_", "_", "_", "_", "_", "_"],
            ["_", "_", "_", "_", "_", "_", "_"],
            ["_", "_", "_", "_", "_", "_", "_"],
            ["_", "_", "_", "_", "_", "_", "_"],
            ["X", "_", "_", "_", "_", "_", "_"],
        ]
            self.assertEqual(test_field1.current_state(), expected)

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
            ["X", "_", "_", "_", "_", "_", "P"],
        ]
        self.assertEqual(test_field2.current_state(), expected)


    def test_legal_move_check2(self):
        test_field4 = Field()
        self.assertEqual(test_field4.check_legal_move(0), False)

        for i in range(6):
            test_field4.set_move(0,"X"):

        x = (test_field4.current_state())
        expected_field1 =[
            ["X", "_", "_", "_", "_", "_", "_"],
            ["X", "_", "_", "_", "_", "_", "_"],
            ["X", "_", "_", "_", "_", "_", "_"],
            ["X", "_", "_", "_", "_", "_", "_"],
            ["X", "_", "_", "_", "_", "_", "_"],
            ["X", "_", "_", "_", "_", "_", "_"],
        ]
            self.assertEqual(x, expected_field1)
            self.assertEqual(test_field4.check_legal_move(0), True)