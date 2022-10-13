'''
Create only odd numbers list.
'''

# Comprehension
# odd_numbers: list = [number for number in range(1, 21, 2)]

# Pylint proposition
odd_numbers: list = list(range(1, 21, 2))

# Print with space
for odd_number in odd_numbers:
    print(odd_number, end=' ')

# Other concept - unpacking a list using '*'
# print(*odd_numbers)
