"""
Simple example of class. The problem here is that we can set invalid value for attribute.
"""


class ClassWithRegularAttributes:
    def __init__(self, some_parameter):
        self.some_attribute = some_parameter


obj = ClassWithRegularAttributes("Some initial value.")
print(obj.some_attribute)
obj.some_attribute = "changed value"
print(obj.some_attribute)
del obj.some_attribute
