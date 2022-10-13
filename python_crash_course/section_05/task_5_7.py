'''
Conditional statements and checks with lists.
'''

fruits: list = ['apple', 'apricot', 'orange', 'banana']

if fruits:
    print("List has elements.")

if 'banana' in fruits:
    print('Should come here.')

if 'grape' not in fruits:
    print('Should come here.')
