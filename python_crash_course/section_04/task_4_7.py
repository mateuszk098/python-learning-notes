'''
Create a list of cubes.
'''

cube_numbers: list = [number**3 for number in range(3, 31)]

for cube_number in cube_numbers:
    print(cube_number)
