'''
Privileges class.
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
