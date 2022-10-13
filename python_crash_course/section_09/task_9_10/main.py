'''
Module import.
'''

from restaurant import Restaurant

if __name__ == '__main__':
    my_res: Restaurant = Restaurant('Galakpizza', 'Pizzeria')
    my_res.description()
