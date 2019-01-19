from src.greed import Greed
import random

from random import randint

if __name__ == '__main__':
    greed = Greed()

    while greed.score_value < 10000:
        dice_values = [random.randint(1, 6) for x in range(1, 6+1)]

        print(dice_values)
        print(str(greed.score(dice_values)) + ' pts.')
        print('----------------------------------------------')
