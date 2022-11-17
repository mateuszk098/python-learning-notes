"""
Simple example of inheritance.
"""


class ParentClass:
    def print_hello(self):
        print("Hello, world!")


class ChildClass(ParentClass):
    def some_new_method(self):
        print("ParentClass doesn't have this method.")


class GrandChildClass(ChildClass):
    def another_new_method(self):
        print("Only GrandChildClass has this method.")


print("Create ParentClass instance and call its method.")
parent = ParentClass()
parent.print_hello()
print()

print("Create ChildClass instance and call its method.")
child = ChildClass()
child.print_hello()
child.some_new_method()
print()

print("Create GrandChildClass instance and call its method.")
grand_child = GrandChildClass()
grand_child.print_hello()
grand_child.some_new_method()
grand_child.another_new_method()
print()

print("Error:")
parent.some_new_method()
