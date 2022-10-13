'''
Conditional statements with loops.
'''

current_users: list = ['Shayna', 'Elta', 'Horacio', 'Terrance', 'Dennis']
new_users: list = ['Greyson', 'Clifford', 'Shayna']

for new_user in new_users:
    if new_user in current_users:
        print('You have to use different name!')
    else:
        print('Approved.')
