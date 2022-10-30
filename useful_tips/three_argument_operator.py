'''
Subtle behaviour of 3-argument operator.
'''

value_if_true: str = 'Authorised Access'
value_if_false: str = 'Permission Denied'
condition: bool = True

msg: str = value_if_true if condition else value_if_false
print(msg)


# Returns 'Permission Denied' if value_if_true = 0, False, None, ''
value_if_true = ''
print(condition and value_if_true or value_if_false)  # type: ignore
