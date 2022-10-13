'''
Class creation, inheritance and use class as atribute.
'''


class Privileges():
    ''' Class pretending privileges. '''

    def __init__(self, privileges: tuple = ('copy file', 'remove file')) -> None:
        self.privileges: tuple = privileges

    def show_privileges(self) -> None:
        ''' Show privileges. '''
        print('This user can:')
        for privilege in self.privileges:
            print(f"- {privilege}")

    def change_privileges(self, new_privileges: tuple) -> None:
        ''' Update privileges. '''
        self.privileges = new_privileges


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


class Admin(User):
    ''' Simple admin inheritance. '''

    def __init__(self, first_name: str, last_name: str) -> None:
        super().__init__(first_name, last_name)
        self.privileges: Privileges = Privileges(('add new user', 'change privileges of user'))
