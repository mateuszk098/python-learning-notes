'''
Convert input from string-list to int/float.
'''

my_lst: list = input().strip().split()  # Default delimiter in split is space
print(my_lst)

# Use map to automatically convert strings
my_converted_lst: list = list(map(int, input().strip().split()))
print(my_converted_lst)
