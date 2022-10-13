'''
Use list cut [:].
'''

numbers: list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

print(f"List - {numbers}")
# First 3 elements
print(f"First 3 elements - {numbers[:3]}")
# Last 3 elements
print(f"Last 3 elements - {numbers[-3:]}")
# Middle 4 elements
mid: int = int(len(numbers)/2)
print(f"Middle 4 elements - {numbers[mid-2:mid+2]}")
# Elements from 2 to 8 skipped by 2
print(f"2 to 8 skipped by 2 - {numbers[1:9:2]}")
# All skipped by 3
print(f"All skipped by 3 - {numbers[::3]}")
