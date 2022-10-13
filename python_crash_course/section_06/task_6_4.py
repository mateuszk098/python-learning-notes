'''
Create dictionary.
'''

elements: dict = {'int': 'Integer number',
                  'str': 'String representation',
                  'for': 'Loop',
                  'if': 'Conditional statement'}

for key, value in elements.items():
    print(f"{key} - {value}")
