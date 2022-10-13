'''
Game die class.
'''

import random


class Die():
    ''' Attempt to simulate a game die. '''

    def __init__(self, sides: int = 6) -> None:
        self.sides: int = sides

    def roll_dice(self) -> int:
        ''' Return the number of die. '''
        return random.randint(1, self.sides)


my_die: Die = Die()
numbers: list[int] = [my_die.roll_dice() for _ in range(10)]
print(numbers)

ten_die: Die = Die(10)
other_numbers: list[int] = [ten_die.roll_dice() for _ in range(10)]
print(other_numbers)
