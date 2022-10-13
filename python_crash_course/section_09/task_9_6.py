'''
Class inheritance.
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
        print(f"Name: {self.res_name}, Type: {self.res_type}, Served: {self.number_served}")

    def open_hours(self) -> None:
        ''' Prints restaurant open-hours. '''
        print('Restaurant is open at 12:00 - 23:00.')

    def set_number_served(self, number_served: int) -> None:
        ''' Set restaurant number serving. '''
        self.number_served = number_served

    def increment_number_served(self) -> None:
        ''' Increment number served by 1. '''
        self.number_served += 1


class IceCreamStand(Restaurant):
    '''
    Simple example of inheritance.
    '''

    def __init__(self, res_name: str, res_type: str) -> None:
        super().__init__(res_name, res_type)  # Initialize from parent class
        self.flavours: list[str] = ['Chocolate', 'Strawberry', 'Vanilla']

    def available_ice_creams(self) -> None:
        ''' Prints available ice creams. '''
        print(f"Avaiable flavours: {self.flavours}")


my_ice_cream_stand: IceCreamStand = IceCreamStand('Chocoloco', 'Ice Creams')
my_ice_cream_stand.description()
my_ice_cream_stand.available_ice_creams()
