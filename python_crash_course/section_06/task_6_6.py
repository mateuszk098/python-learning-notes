'''
Create dictionary. Check elements.
'''

languages: dict = {'Jennifer': 'C++', 'Hadley': 'Python'}
# Add element to dict
languages['Laney'] = 'Java'
print(languages)

new_users: tuple = ('Hellen', 'Jennifer', 'Claire')

for user in new_users:
    if user in languages.keys():
        print(f"{user} already exists.")
    else:
        print(f"{user} you are new here.")
