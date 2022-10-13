'''
Methods `setattr` and `getattr` in class.
'''


class Person:
    pass


person: Person = Person()
person_info: dict[str, str] = {"first": "Corey", "last": "Schafer"}

# Set attributes
for key, value in person_info.items():
    setattr(person, key, value)

# Read attributes
for key, value in person_info.items():
    print(getattr(person, key, value))
