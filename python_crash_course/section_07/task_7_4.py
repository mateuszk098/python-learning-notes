'''
Communication with user with while loop.
'''

while True:
    ingredient: str = input("Enter the ingredient you want or 'end' to quit: ")

    if ingredient == 'end':
        break

    print(f"You added {ingredient}!")
