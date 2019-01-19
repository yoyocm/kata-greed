import sys
import os
import unittest
sys.path.append(os.path.abspath('..'))
from src.greed import Greed


class GreedTest(unittest.TestCase):
    def test_greed_init(self):
        """ test greed init"""

        values = {
            "1": 0,
            "2": 0,
            "3": 0,
            "4": 0,
            "5": 0,
            "6": 0
        }

        greed = Greed()
        self.assertEqual(greed.score, 0)
        self.assertEqual(greed.number_of_dices, 6)
        self.assertEqual(greed.min_dice_value, 1)
        self.assertEqual(greed.max_dice_value, 6)
        self.assertEqual(greed.values, values)

        values = {
            "2": 0,
            "3": 0,
            "4": 0,
        }

        greed = Greed(number_of_dices=5, min_dice_value=2, max_dice_value=4)
        self.assertEqual(greed.score, 0)
        self.assertEqual(greed.number_of_dices, 5)
        self.assertEqual(greed.min_dice_value, 2)
        self.assertEqual(greed.max_dice_value, 4)
        self.assertEqual(greed.values, values)

    def test_increment_value(self):
        greed = Greed()
        greed._increment_value(1)
        greed._increment_value(3)
        greed._increment_value(1)
        greed._increment_value(6)

        values = {
            "1": 2,
            "2": 0,
            "3": 1,
            "4": 0,
            "5": 0,
            "6": 1
        }

        self.assertEqual(greed.values, values)

    def test_reset_values(self):
        greed = Greed()

        greed._increment_value(1)
        greed._increment_value(3)
        greed._increment_value(1)
        greed._increment_value(6)

        greed._reset_values()

        values = {
            "1": 0,
            "2": 0,
            "3": 0,
            "4": 0,
            "5": 0,
            "6": 0
        }

        self.assertEqual(greed.values, values)


if __name__ == '__main__':
    unittest.main()
