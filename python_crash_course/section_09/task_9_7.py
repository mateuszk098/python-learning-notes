'''
Class inheritance.
'''


class User():
    ''' Simple user class. '''

    def __init__(self, first_name: str, last_name: str) -> None:
        self.first_name: str = first_name
        self.last_name: str = last_name
        self.age: int = 24
        self.sex: str = 'male'
        self.login_attemps: int = 0

    def greet_user(self) -> None:
        ''' Prints informations about user. '''
        print('User Informations:')
        print(f"First Name: {self.first_name}")
        print(f"Last Name: {self.last_name}")
        print(f"Age: {self.age}")
        print(f"Sex: {self.sex}")
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
        self.privileges: tuple = ('add new user', 'change privileges of user')

    def show_privileges(self) -> None:
        ''' Prints admin privileges. '''
        print('This is admin account. You can:')
        for privilege in self.privileges:
            print(f"- {privilege}")


admin: Admin = Admin('Koby', 'Fisher')
admin.show_privileges()
