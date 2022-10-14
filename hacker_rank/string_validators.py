if __name__ == '__main__':
    s = input()

    for action in ['isalnum()', 'isalpha()', 'isdigit()', 'islower()', 'isupper()']:
        state = False
        for letter in s:
            if eval(f'letter.{action}'):
                state = True
                break
        print(state)
