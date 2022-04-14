import unittest
from game.game import *


class MyTestCase(unittest.TestCase):
    """checks if the field is initiated right once an object is created from the class field"""

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

    """Checks if the quit function returns true in upper and lower case "q" input
    Also checks if False is returned in case of other type of input"""

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

    """checks if input is legal to the rules
    More specific instruction above the assertEquals calls"""

    def test_legal_move_check(self):

        test_field = Field()

        """check if input was int
        Only the case in which an illegal move is made needs to be checked. The function does not return true in
        case that the input was an int and proceeds with further checks """
        input_str = "g"
        self.assertEqual(test_field.check_legal_move(input_str), True)

        """checks if input out of range of the field is rejected
        :returns True if out of bounce otherwise nothing is returned"""
        input_to_small = -5
        input_to_large = 8
        self.assertEqual(test_field.check_legal_move(input_to_small), True)
        self.assertEqual(test_field.check_legal_move(input_to_large), True)

    """checks if moves are executed right in the Field object"""

    def test_set_move(self):
        test_field1 = Field()

        """Adds an X to the 0th column"""
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
        """Adds an P to the 6th column"""
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
        """Checks if stacking on top works"""
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

    """checks of the selected column has still space 
    :returns True if there is no space otherwise False if there is still space
    set_move method is used but is tested earlier so due to transitivity can be applied here"""

    def test_legal_move_check2(self):
        test_field4 = Field()
        self.assertEqual(test_field4.check_legal_move(0), False)

        """Adding 6 Symbols in column 0 so there is no space left
        :returns True in case there is no space left"""
        for i in range(6):
            test_field4.set_move(0, "X")

        """checks if one column is successfully filled"""
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
        """should return true if column is filled"""
        self.assertEqual(test_field4.check_legal_move(0), True)

    """checks if a game contains four in a row of any kind
    :returns True if it is the case"""

    def test_check_if_win(self):
        # vertical
        field5 = Field()
        for i in range(4):
            field5.set_move(0, "X")

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

    """The print_field does not need to be tested"""


if __name__ == '__main__':
    unittest.main()
