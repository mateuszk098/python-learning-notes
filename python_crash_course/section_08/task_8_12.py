'''
Simple function with *args.
'''


# Argument *args tells Python to create empty tuple
# and put every arg in this tuple.
def sandwich_orders(*args) -> None:
    '''
    Prints all arguments.
    '''
    print(args)


sandwich_orders('Tomato')
sandwich_orders('Ham', 'Cheese')
sandwich_orders('Pepperoni', 'Chorizo', 'Ham')
