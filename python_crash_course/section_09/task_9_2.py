'''
Create simple class.
'''


class Restaurant():
    '''
    Simple restaurant type.
    '''

    def __init__(self, res_name: str, res_type: str) -> None:
        self.res_name: str = res_name
        self.res_type: str = res_type

    def description(self) -> None:
        ''' Prints simple class description. '''
        print(f"Name: {self.res_name} - Type: {self.res_type}")

    def open_hours(self) -> None:
        ''' Prints restaurant open-hours. '''
        print('Restaurant is open at 12:00 - 23:00.')


my_restaurant_1: Restaurant = Restaurant('Galakpizza', 'Pizzeria')
my_restaurant_2: Restaurant = Restaurant('K1', 'Burgers')
my_restaurant_3: Restaurant = Restaurant('Japa', 'Japan')

my_restaurant_1.description()
my_restaurant_2.description()
my_restaurant_3.description()
