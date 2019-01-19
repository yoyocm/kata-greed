from typing import List


class Greed():

    def __init__(
            self,
            number_of_dices: int = 6,
            min_dice_value: int = 1,
            max_dice_value: int = 6
    ):
        self.score = 0
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
        for v in dice_values:
            if v < self.min_dice_value or v > self.max_dice_value:
                raise ValueError("Dice can not take this value.")

            self._increment_value(v)

    def score(self, dice_values: List[int]):
        if len(dice_values) != self.number_of_dices:
            raise ValueError("Number of dice values is different \
                             of the declared number of dices.")

        self._reset_values()
