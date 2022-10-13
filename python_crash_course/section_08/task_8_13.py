'''
Simple function with **kwargs.
'''


# Argument *args tells Python to create empty dictionary
# and put every kwarg in this dictionary.
def build_profile(first: str, last: str, **kwargs) -> dict:
    '''
    Build simple dictionary about user.
    '''
    kwargs['First Name'] = first
    kwargs['Last Name'] = last
    return kwargs


my_profile: dict = build_profile('Colby', 'Welch', age=30, sex='Male')
print(my_profile)
