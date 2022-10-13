'''
Special library to password handle.
'''

from getpass import getpass

login: str = input('Enter login: ')
password: str = getpass('Enter password: ')  # Password is not visible

print('Loggin in...')
