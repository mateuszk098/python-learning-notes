"""
Example of conversion of an attribute into a property.
"""


class ClassWithProperty:
    def __init__(self):
        self.some_attribute = "Some initial value."

    # Here we have _some_attribute, which is called a backing variable.

    @property
    def some_attribute(self):  # This is getter.
        return self._some_attribute

    @some_attribute.setter
    def some_attribute(self, value):  # This is setter.
        self._some_attribute = value

    @some_attribute.deleter
    def some_attribute(self):  # This is deleter.
        del self._some_attribute


obj = ClassWithProperty()
print(obj.some_attribute)
obj.some_attribute = "changed value"
print(obj.some_attribute)
del obj.some_attribute
