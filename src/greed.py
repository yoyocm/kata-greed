from typing import List


class Greed():

    def __init__(
            self,
            number_of_dices: int = 6,
            min_dice_value: int = 1,
            max_dice_value: int = 6
    ):
        self.score_value = 0
        self.number_of_dices = number_of_dices
        self.min_dice_value = min_dice_value
        self.max_dice_value = max_dice_value
        self.values = {}

        for i in range(self.min_dice_value, self.max_dice_value+1):
            self.values[str(i)] = 0

    def _reset_values(self):
        self.values = {}
        for i in range(self.min_dice_value, self.max_dice_value+1):
            self.values[str(i)] = 0

    def _increment_value(self, value: int):
        self.values[str(value)] += 1

    def _fill_values(self, dice_values: List[int]):
        self._reset_values()

        for v in dice_values:
            if v < self.min_dice_value or v > self.max_dice_value:
                raise ValueError("Dice can not take this value.")

            self._increment_value(v)

    def _is_single_one(self):
        return self.values["1"] == 1

    def _is_single_five(self):
        return self.values["5"] == 1

    def _is_triple_with_value(self, dice_value: int):
        return self.values[str(dice_value)] == 3

    def _is_a_kind(self, number_of_values: int):
        for i in range(self.min_dice_value, self.max_dice_value + 1):
            if self.values[str(i)] == number_of_values:
                return True

        return False

    def _is_three_pairs(self):
        number_of_pairs = 0

        for key, value in self.values.items():
            if value == 2:
                number_of_pairs += 1

        return number_of_pairs == 3

    def _is_straigth(self):
        for i in range(self.min_dice_value, self.max_dice_value + 1):
            if self.values[str(i)] < 1:
                return False

        return True

    def score(self, dice_values: List[int]):
        if len(dice_values) != self.number_of_dices:
            raise ValueError("Number of dice values is different \
                             of the declared number of dices.")

        self._fill_values(dice_values)

        # Check if there is a kind
        multiplicator = 2
        for i in range(4, self.max_dice_value + 1):
            if self._is_a_kind(i):
                self.score_value *= multiplicator
                return self.score_value
            multiplicator *= 2

        # Check if there is a straight
        if self._is_straigth():
            self.score_value += 1200
            return self.score_value

        # Check if there is three paires
        if self._is_three_pairs():
            self.score_value += 800
            return self.score_value

        # Check if there is a triple ones
        if self._is_triple_with_value(1):
            self.score_value += 1000

        # Check if there is a triple
        for i in range(2, self.max_dice_value):
            if self._is_triple_with_value(i):
                self.score_value += 100 * i

        # Check if there is a single five
        if self._is_single_five():
            self.score_value += 50

        # Check if there is a single one
        if self._is_single_one():
            self.score_value += 100

        return self.score_value
