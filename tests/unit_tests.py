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

