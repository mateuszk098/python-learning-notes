'''
Simple function. Default values
'''


def make_shirt(size: str = 'XL', text: str = 'Python') -> None:
    '''
    Print informations about t-shirt.
    '''
    print(f"Size: {size}, Text: {text}")


my_size: str = 'M'
my_text: str = 'VSCode'

# Without args
make_shirt()
# With positional args - order is important
make_shirt(my_size, my_text)
# With key arguments - order is not important
make_shirt(size=my_size, text=my_text)
make_shirt(text=my_text, size=my_size)
