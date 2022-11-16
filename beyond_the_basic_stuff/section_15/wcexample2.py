"""
WizCoin test.
"""

import wizcoin

change = wizcoin.WizCoin(9, 7, 20)
print(change.sickles)
change.sickles += 10
print(change.sickles)

pile = wizcoin.WizCoin(2, 3, 31)
print(pile.sickles)
pile.some_new_attribute = "new_attribute"
print(pile.some_new_attribute)
