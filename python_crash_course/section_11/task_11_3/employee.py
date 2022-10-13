'''
Simple class representing a employee.
'''


class Employee():
    ''' Simple class representing a employee. '''

    def __init__(self, first_name: str, last_name: str, annual_raise: int) -> None:
        self.first_name: str = first_name
        self.last_name: str = last_name
        self.annual_raise: int = annual_raise

    def give_raise(self, my_raise: int = 5000) -> None:
        ''' Give a raise. '''
        self.annual_raise += my_raise

    def get_raise(self) -> int:
        ''' Return the raise. '''
        return self.annual_raise
