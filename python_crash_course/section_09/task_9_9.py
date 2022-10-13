'''
Class creation, inheritance and use class as atribute.
'''


class Car():
    ''' Simple representation of a car. '''

    def __init__(self, make: str, model: str, year: int) -> None:
        self.make: str = make
        self.model: str = model
        self.year: int = year
        self.odometer: int = 0

    def get_description(self) -> str:
        ''' Return descriptive name of the car. '''
        name: str = f"{self.make} {self.model} {self.year} {self.odometer} km."
        return name

    def read_odometer(self) -> None:
        ''' Print the odometer information. '''
        print(f"This cas has travelled {self.odometer} km.")

    def update_odometer(self, mileage: int) -> None:
        ''' Update the odometer information. '''
        if mileage <= self.odometer:
            print("Cannot reverse odometer.")
            return
        self.odometer = mileage

    def increment_odometer(self, kilometers: int) -> None:
        ''' Increment the odometer. '''
        if kilometers <= 0:
            print("Cannot increment odometer.")
            return
        self.odometer += kilometers


class Battery():
    ''' Representation of a battery. '''

    def __init__(self, battery_size: int = 75) -> None:
        self.battery_size: int = battery_size

    def get_battery_size(self) -> int:
        ''' Return battery size. '''
        return self.battery_size

    def get_battery_range(self) -> int:
        ''' Return battery range. '''
        if self.battery_size == 75:
            return 260
        if self.battery_size == 100:
            return 315
        return 0

    def upgrade_battery(self) -> None:
        ''' Upgrade the battery. '''
        if self.battery_size != 100:
            self.battery_size = 100


class ElectricCar(Car):
    ''' Simple inheritance to represent an electric car. '''

    def __init__(self, make: str, model: str, year: int) -> None:
        super().__init__(make, model, year)
        self.battery: Battery = Battery()


my_car: ElectricCar = ElectricCar('Tesla', 'Model S', 2022)
my_car_desc: str = my_car.get_description()
my_car_battery: int = my_car.battery.get_battery_size()
my_car_range: int = my_car.battery.get_battery_range()

print(my_car_desc)
print(my_car_battery)
print(my_car_range)


my_car.battery.upgrade_battery()
my_car_battery = my_car.battery.get_battery_size()
my_car_range = my_car.battery.get_battery_range()
print(my_car_battery)
print(my_car_range)
