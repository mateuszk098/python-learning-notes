"""
WizCoin test.
"""

import wizcoin

purse = wizcoin.WizCoin(2, 5, 99)
print("Purse:", purse)
print("G:", purse.galleons, "S:", purse.sickles, "K:", purse.knuts)
print("Total value:", purse.value())
print("Weight:", purse.weight_in_grams(), "grams.")

print()

coin_jar = wizcoin.WizCoin(13, 0, 0)
print("Coin Jar:", coin_jar)
print("G:", coin_jar.galleons, "S:", coin_jar.sickles, "K:", coin_jar.knuts)
print("Total value:", coin_jar.value())
print("Weight:", coin_jar.weight_in_grams(), "grams.")
