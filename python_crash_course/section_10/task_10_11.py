'''
Simple .json use.
'''

import json


favourite_number: str = input('Enter your favourite number: ')

# Save
with open(file='file_task_10_11.json', mode='w', encoding='utf-8') as f:
    json.dump(favourite_number, f)

# Read
with open(file='file_task_10_11.json', mode='r', encoding='utf-8') as f:
    number: str = json.load(f)

print(number)
