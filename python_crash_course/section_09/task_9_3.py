'''
Create simple class.
'''


class User():
    ''' Simple user class. '''

    def __init__(self, first_name: str, last_name: str) -> None:
        self.first_name: str = first_name
        self.last_name: str = last_name
        self.age: int = 24
        self.sex: str = 'male'

    def greet_user(self) -> None:
        ''' Prints informations about user. '''
        print('User Informations:')
        print(f"First Name: {self.first_name}")
        print(f"Last Name: {self.last_name}")
        print(f"Age: {self.age}")
        print(f"Sex: {self.sex}")


my_user: User = User('Zoila', 'Huels')
my_user.greet_user()
