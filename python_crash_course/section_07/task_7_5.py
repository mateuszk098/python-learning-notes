'''
Communication with user with while loop.
'''

while True:
    age: int = int(input("Enter your age: "))

    if age <= 3:
        print('For you the ticket is free.')
    elif 3 < age <= 12:
        print('You have to pay 3 PLN.')
    else:
        print('You have to pay 5 PLN.')
