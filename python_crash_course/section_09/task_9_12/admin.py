'''
Class creation, inheritance and use class as atribute.
'''

from user import User
from privileges import Privileges


class Admin(User):
    ''' Simple admin inheritance. '''

    def __init__(self, first_name: str, last_name: str) -> None:
        super().__init__(first_name, last_name)
        self.privileges: Privileges = Privileges(('add new user', 'change privileges of user'))
