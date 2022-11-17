"""
Simple WizCoin class.

Add properties.
Properties are used usually when we have to validate data format.
That provides early detection of errors.

Add dunder methods (magic methods).

Representation dunder methods.
Numerical dunder methods.
Reflected numerical dunder methods.
Numberical dunder methods in-place.
Comparison dunder methods.

These are methods with double underscore __.
Dunder methods provide operators overloading and usage
of built-in functions like as `str()` or `repr()`.

Numerical dunder methods for operators like as '+', '-', '*', '**', etc.
always should create a new object.

Numerical dunder methods in-place for operators like as '+=', '-=', '*=',
modify the object in-place.
"""

import collections.abc
import operator


class WizCoinException(Exception):
    """Raises this exception when the module is used invalid."""
    pass


class WizCoin:
    def __init__(self, galleons, sickles, knuts):
        """Creates a new WizCoin object."""
        self.galleons = galleons
        self.sickles = sickles
        self.knuts = knuts

    @property
    def weight_in_grams(self):
        """Returns all coins weight in grams."""
        return (self.galleons * 31.103) + (self.sickles * 11.34) + (self.knuts * 5.0)

    @property
    def total_value(self):  # Only to read.
        """Returns value of all coins in knuts."""
        return (self.galleons * 17 * 29) + (self.sickles * 29) + (self.knuts)

    @property
    def galleons(self):
        """Returns galleons number saved in this object."""
        return self._galleons

    @galleons.setter
    def galleons(self, value):
        if not isinstance(value, int):
            raise WizCoinException(
                f"The `galleons` attribute must be set to 'int' value, "
                f"not to '{value.__class__.__qualname__}'.")
        if value < 0:
            raise WizCoinException(
                f"The `galleons` attribute must be positive 'int' value, "
                f"not negative '{value.__class__.__qualname__}' value.")
        self._galleons = value

    @property
    def sickles(self):
        """Returns sickles number saved in this object."""
        return self._sickles

    @sickles.setter
    def sickles(self, value):
        if not isinstance(value, int):
            raise WizCoinException(
                f"The `sickles` attribute must be set to 'int' value, "
                f"not to '{value.__class__.__qualname__}'.")
        if value < 0:
            raise WizCoinException(
                f"The `sickles` attribute must be positive 'int' value, "
                f"not negative '{value.__class__.__qualname__}' value.")
        self._sickles = value

    @property
    def knuts(self):
        """Returns knuts number saved in this object."""
        return self._knuts

    @knuts.setter
    def knuts(self, value):
        if not isinstance(value, int):
            raise WizCoinException(
                f"The `knuts` attribute must be set to 'int' value, "
                f"not to '{value.__class__.__qualname__}'.")
        if value < 0:
            raise WizCoinException(
                f"The `knuts` attribute must be positive 'int' value, "
                f"not negative '{value.__class__.__qualname__}' value.")
        self._knuts = value

    # REPRESENTATION DUNDER METHODS.

    def __repr__(self):
        """Returns the canonical string representation of the object."""
        return f"{self.__class__.__qualname__}({self.galleons}, {self.sickles}, {self.knuts})"

    def __str__(self):
        """Returns string representation of the object."""
        return f"{self.galleons}G, {self.sickles}S, {self.knuts}K"

    # NUMERICAL DUNDER METHODS.

    def __add__(self, other):
        """Returns a new WizCoin object, which is sum of two WizCoin objects."""
        if not isinstance(other, WizCoin):
            return NotImplemented
        return WizCoin(self.galleons + other.galleons, self.sickles + other.sickles, self.knuts + other.knuts)

    def __sub__(self, other):
        """Returns a new WizCoin object, which is difference of two WizCoin objects."""
        if not isinstance(other, WizCoin):
            return NotImplemented
        return WizCoin(self.galleons - other.galleons, self.sickles - other.sickles, self.knuts - other.knuts)

    # When we have e.g. WizCoin(1, 1, 1) * 2.
    def __mul__(self, other):
        """Returns a new WizCoin object, which is product of WizCoin and int objects."""
        if not isinstance(other, int):
            return NotImplemented
        if other < 0:
            raise WizCoinException("Multiplication by negative value is not allowed.")
        return WizCoin(self.galleons * other, self.sickles * other, self.knuts * other)

    def __pow__(self, other):
        """Returns a new WizCoin object, which is power of WizCoin to int value."""
        if not isinstance(other, int):
            return NotImplemented
        if other < 0:
            raise WizCoinException("Power to negative value is not allowed.")
        return WizCoin(self.galleons ** other, self.sickles ** other, self.knuts ** other)

    # REFLECTED NUMERICAL DUNDER METHODS.

    # When we have e.g. 2 * WizCoin(1, 1, 1).
    def __rmul__(self, other):
        return self.__mul__(other)

    # NUMERICAL DUNDER METHODS IN-PLACE.

    # IMPORTANT: IF YOU DO NOT IMPLEMENT IN-PLACE DUNDER METHODS
    # THEN E.G. CODE:
    # p = WizCoin(1, 1, 1)
    # p *= 2
    # WILL RESULT IN CALLING `__mul__()` METHOD AND ITS RESULT WILL BE ASSIGNED
    # TO THE `p` VARIABLE.

    def __iadd__(self, other):
        """Adds coins from other WizCoin object to this WizCoin object."""
        if not isinstance(other, WizCoin):
            return NotImplemented

        self.galleons += other.galleons
        self.sickles += other.sickles
        self.knuts += other.knuts

        return self

    def __imul__(self, other):
        """Multiply coins in this WizCoin object by int value."""
        if not isinstance(other, int):
            return NotImplemented
        if other < 0:
            raise WizCoinException("Multiplication by negative value is not allowed.")

        self.galleons *= other
        self.sickles *= other
        self.knuts *= other

        return self

    # COMPARISON DUNDER METHODS.

    def _comparison_operator_helper(self, operator_func, other):
        """Help method for comparison dunder methods."""
        if isinstance(other, WizCoin):
            return operator_func(self.total_value, other.total_value)
        elif isinstance(other, (int, float)):
            return operator_func(self.total_value, other)
        elif isinstance(other, collections.abc.Sequence):
            other_value = (other[0] * 17 * 29) + (other[1] * 29) + other[2]
            return operator_func(self.total_value, other_value)
        elif operator_func == operator.eq:
            return False
        elif operator_func == operator.ne:
            return True
        else:
            return NotImplemented

    def __eq__(self, other):  # Equal.
        return self._comparison_operator_helper(operator.eq, other)

    def __ne__(self, other):  # Not Equal.
        return self._comparison_operator_helper(operator.ne, other)

    def __lt__(self, other):  # Less Than.
        return self._comparison_operator_helper(operator.lt, other)

    def __le__(self, other):  # Less Equal.
        return self._comparison_operator_helper(operator.le, other)

    def __gt__(self, other):  # Greater Than.
        return self._comparison_operator_helper(operator.gt, other)

    def __ge__(self, other):  # Greaten Equal.
        return self._comparison_operator_helper(operator.ge, other)
