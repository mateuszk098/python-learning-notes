'''
Check if the value has one of the different values.
'''

foo: str = 'cat'

if foo == 'dog' or foo == 'cat' or foo == 'deer':
    print(True)

# Pythonic way
if 'cat' in ('dog', 'cat', 'deer'):
    print(True)
