'''
Create a list and use of min(), max(), sum().
'''

# Comprehension
# numbers: list = [number for number in range(1, 1_000_001)]

# Pylint proposition
numbers: list = list(range(1, 1_000_001))

print(f"Min value - {min(numbers)}")
print(f"Max value - {max(numbers)}")
print(f"Numbers sum - {sum(numbers)}")
