'''
Simple .json use.
'''

import json

fname: str = input('Enter filename: ')

try:
    # Read
    with open(file=fname, mode='r', encoding='utf-8') as f:
        number: str = json.load(f)
except FileNotFoundError:
    print('File not found!')
    favourite_number: str = input('Enter your favourite number: ')
    # Save
    with open(file='file_task_10_11.json', mode='w', encoding='utf-8') as f:
        json.dump(favourite_number, f)
else:
    print(number)
