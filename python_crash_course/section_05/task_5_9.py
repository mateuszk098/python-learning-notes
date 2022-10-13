'''
Conditional statements with loops.
'''

users: list = []

if users:  # List has elements?
    for user in users:
        if user == 'Admin':
            print('Hello Admin. Would you like to see daily report?')
        else:
            print(f"Hello {user}.")
else:  # List is empty
    print('We should find any user.')
