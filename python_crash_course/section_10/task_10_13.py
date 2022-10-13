'''
Simple .json use.
'''

import json
import sys


def get_stored_username() -> str | None:
    ''' Load username from file if it exists. '''
    filename: str = 'file_task_10_13.json'
    try:
        with open(file=filename, mode='r', encoding='utf8') as f:
            username: str = json.load(f)
    except FileNotFoundError:
        return None
    else:
        return username


def get_new_username() -> str:
    ''' Request for username and save it to .json file. '''
    username: str = input('Enter your name: ')
    filename: str = 'file_task_10_13.json'
    with open(file=filename, mode='w', encoding='utf8') as f:
        json.dump(username, f)
    return username


def greet_user() -> None:
    ''' Print greeting to user using username. '''
    username: str | None = get_stored_username()

    if username is not None:
        print(f'Username: {username}')
    else:
        username = get_new_username()
        print('Your username has been stored.')
        sys.exit()

    answer: str = input('Is your username correct? (y/n): ')
    if answer == 'y':
        print(f"Welcome {username}!")
    else:
        username = get_new_username()
        print('Your username has been stored.')


if __name__ == '__main__':
    greet_user()
