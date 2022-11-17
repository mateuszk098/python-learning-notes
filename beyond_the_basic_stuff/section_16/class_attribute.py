"""
Simple example of class attribute.
Class attribute is defined beyond all class methods.
Class attibute may be used as a class constant. 
E.g. Oval class may have PI = 3.14 class attribute.
"""


class CreateCounter:
    count = 0  # Class attribute.

    def __init__(self):
        CreateCounter.count += 1


print("Objects:", CreateCounter.count)
a = CreateCounter()
b = CreateCounter()
print("Objects:", CreateCounter.count)
