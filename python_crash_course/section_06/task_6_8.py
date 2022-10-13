'''
Embedd dictionaries in lists.
'''

cat: dict = {'Pet': 'Dog', 'Name': 'Nils', 'age': 2}
dog: dict = {'Pet': 'Cat', 'Name': 'Blanche', 'age': 4}

animals: list = [cat, dog]

for animal in animals:
    for key, value in animal.items():
        print(f"{key} - {value}")
