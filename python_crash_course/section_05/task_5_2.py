'''
Conditional statements and checks.
'''

sentence_1: str = 'Success in programming critically depends on presented solutions.'
sentence_2: str = 'Success in programming critically depends on presented solutions.'
print(f"sentence_1 == sentence_2: {sentence_1 == sentence_2}")

numbers: list = [1, 2, 3, 4, 5]
print(f"Number 2 in numbers: {2 in numbers}")
print(f"Number 2 not in numbers: {2 not in numbers}")
print(f"Number 8 not in numbers: {8 not in numbers}")
print(f"Numbers length is between 4 and 7: {4 < len(numbers) < 7}")
