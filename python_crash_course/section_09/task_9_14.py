'''
Lottery class.
'''

import random


class Lottery():
    ''' Attempt to simulate a lottery. '''

    # Private list (two _)
    __signs: list = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k',
                     'l', 'm', 'n', 'o', 'p', 'r', 's', 't', 'u', 'v', 'w',
                     'x', 'y', 'z', '1', '2', '3', '4', '5', '6', '7', '8', '9']

    def __init__(self, chars: int = 10) -> None:
        self.chars: int = chars

    def generate_ticket(self) -> str:
        ''' Return random ticket. '''
        rand_ticket: str = ''
        for _ in range(self.chars):
            rand_ticket += random.choice(self.__signs)
        return rand_ticket


my_lottery: Lottery = Lottery()
my_ticket: str = my_lottery.generate_ticket()
print(my_ticket)
