'''
Embedd dictionaries in lists.
'''

first_person: dict = {'first_name': 'John', 'last_name': 'Spencer', 'age': 25}
second_person: dict = {'first_name': 'Wilfred', 'last_name': 'Lehner', 'age': 22}
third_person: dict = {'first_name': 'Hector', 'last_name': 'Pfeffer', 'age': 24}

persons: list = [first_person, second_person, third_person]

for person in persons:
    for key, value in person.items():
        print(f"{key} - {value}")
