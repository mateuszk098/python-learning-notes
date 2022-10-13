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
        self.number_served: int = 0

    def description(self) -> None:
        ''' Prints simple class description. '''
        print(f"Name: {self.res_name} - Type: {self.res_type} - Served: {self.number_served}")

    def open_hours(self) -> None:
        ''' Prints restaurant open-hours. '''
        print('Restaurant is open at 12:00 - 23:00.')

    def set_number_served(self, number_served: int) -> None:
        ''' Set restaurant number serving. '''
        self.number_served = number_served

    def increment_number_served(self) -> None:
        ''' Increment number served by 1. '''
        self.number_served += 1


my_restaurant: Restaurant = Restaurant('Galakpizza', 'Pizzeria')
my_restaurant.description()
my_restaurant.open_hours()

# Direct change of parameter
my_restaurant.number_served = 5
my_restaurant.description()

# Change by method
my_restaurant.set_number_served(10)
my_restaurant.description()

# Increment
my_restaurant.increment_number_served()
my_restaurant.description()
