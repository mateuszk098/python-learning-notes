'''
If-else statement in one line.
'''

condition: bool = True
my_number: int = 0

# Typical if-else statement
if condition:
    my_number = 1
else:
    my_number = -1
print(my_number)

# Oneline if-else statement
my_number = 2 if condition else -2
print(my_number)
