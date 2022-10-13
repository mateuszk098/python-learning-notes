'''
User class.
'''

from privileges import Privileges


class User():
    ''' Simple user class. '''

    def __init__(self, first_name: str, last_name: str) -> None:
        self.first_name: str = first_name
        self.last_name: str = last_name
        self.login_attemps: int = 0
        self.privileges: Privileges = Privileges()  # Use class as atribute

    def greet_user(self) -> None:
        ''' Prints informations about user. '''
        print('User Informations:')
        print(f"First Name: {self.first_name}")
        print(f"Last Name: {self.last_name}")
        print(f"Login Attemps: {self.login_attemps}")

    def increment_login_attemps(self) -> None:
        ''' Increment login attemps by  1.'''
        self.login_attemps += 1

    def reset_login_attemps(self) -> None:
        ''' Reset login attemps. '''
        self.login_attemps = 0
