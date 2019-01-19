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
        self.assertEqual(greed.score_value, 0)
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
        self.assertEqual(greed.score_value, 0)
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

    def test_fill_values(self):
        greed = Greed()
        dice_values = [1, 2, 3, 2, 5, 4]
        values = {
            "1": 1,
            "2": 2,
            "3": 1,
            "4": 1,
            "5": 1,
            "6": 0
        }

        greed._fill_values(dice_values)
        self.assertEquals(greed.values, values)

    def test_single_one(self):
        greed = Greed()

        dice_values = [1, 2, 3, 2, 5, 4]
        greed._fill_values(dice_values)
        self.assertTrue(greed._is_single_one())

        dice_values = [1, 1, 3, 2, 5, 4]
        greed._fill_values(dice_values)
        self.assertFalse(greed._is_single_one())

    def test_single_five(self):
        greed = Greed()

        dice_values = [1, 2, 3, 2, 5, 4]
        greed._fill_values(dice_values)
        self.assertTrue(greed._is_single_five())

        dice_values = [1, 1, 3, 2, 5, 5]
        greed._fill_values(dice_values)
        self.assertFalse(greed._is_single_five())

    def test_triple(self):
        greed = Greed()

        dice_values = [1, 2, 3, 2, 5, 4]
        greed._fill_values(dice_values)
        self.assertFalse(greed._is_triple_with_value(1))

        dice_values = [1, 1, 1, 2, 5, 5]
        greed._fill_values(dice_values)
        self.assertTrue(greed._is_triple_with_value(1))

        dice_values = [1, 1, 3, 2, 5, 1]
        greed._fill_values(dice_values)
        self.assertTrue(greed._is_triple_with_value(1))

        dice_values = [1, 1, 3, 2, 1, 1]
        greed._fill_values(dice_values)
        self.assertFalse(greed._is_triple_with_value(1))

    def test_kind(self):
        greed = Greed()

        dice_values = [1, 2, 3, 2, 5, 4]
        greed._fill_values(dice_values)
        self.assertFalse(greed._is_a_kind(4))

        dice_values = [1, 2, 3, 2, 2, 4]
        greed._fill_values(dice_values)
        self.assertFalse(greed._is_a_kind(4))

        dice_values = [2, 2, 3, 2, 2, 4]
        greed._fill_values(dice_values)
        self.assertTrue(greed._is_a_kind(4))

        dice_values = [1, 1, 1, 2, 1, 1]
        greed._fill_values(dice_values)
        self.assertTrue(greed._is_a_kind(5))

        dice_values = [1, 1, 1, 1, 1, 1]
        greed._fill_values(dice_values)
        self.assertTrue(greed._is_a_kind(6))

    def test_three_pairs(self):
        greed = Greed()

        dice_values = [1, 2, 3, 2, 5, 4]
        greed._fill_values(dice_values)
        self.assertFalse(greed._is_three_pairs())

        dice_values = [1, 1, 2, 2, 3, 3]
        greed._fill_values(dice_values)
        self.assertTrue(greed._is_three_pairs())

        dice_values = [1, 1, 1, 1, 1, 1]
        greed._fill_values(dice_values)
        self.assertFalse(greed._is_three_pairs())

        dice_values = [1, 2, 3, 3, 2, 1]
        greed._fill_values(dice_values)
        self.assertTrue(greed._is_three_pairs())

        dice_values = [1, 2, 3, 1, 2, 3]
        greed._fill_values(dice_values)
        self.assertTrue(greed._is_three_pairs())

    def test_straight(self):
        greed = Greed()

        dice_values = [1, 2, 3, 2, 5, 4]
        greed._fill_values(dice_values)
        self.assertFalse(greed._is_straigth())

        dice_values = [1, 2, 3, 4, 5, 6]
        greed._fill_values(dice_values)
        self.assertTrue(greed._is_straigth())

        dice_values = [4, 1, 6, 3, 2, 5]
        greed._fill_values(dice_values)
        self.assertTrue(greed._is_straigth())

    def test_score(self):
        greed = Greed()

        dice_values = [1, 2, 3, 4, 5, 6]
        score = greed.score(dice_values)
        self.assertEquals(score, 1200)

if __name__ == '__main__':
    unittest.main()
