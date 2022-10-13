'''
Conditional statements with loops.
'''

users: tuple = ('Wilber', 'John', 'Marcella', 'Admin')

for user in users:
    if user == 'Admin':
        print('Hello Admin. Would you like to see daily report?')
    else:
        print(f"Hello {user}.")
