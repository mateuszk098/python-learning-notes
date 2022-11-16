"""
Simple WizCoin class.
"""


class WizCoin:
    def __init__(self, galleons, sickles, knuts):
        """Creates a new WizCoin object."""
        self.galleons = galleons
        self.sickles = sickles
        self.knuts = knuts

    def value(self):
        """Returns value of all coins in knuts."""
        return (self.galleons * 17 * 29) + (self.sickles * 29) + (self.knuts)

    def weight_in_grams(self):
        """Returns all coins weight in grams."""
        return (self.galleons * 31.103) + (self.sickles * 11.34) + (self.knuts * 5.0)
