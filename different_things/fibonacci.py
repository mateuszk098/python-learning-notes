''' Calculate n-th fibonacci number. '''

import sys
from functools import lru_cache


# Cache remembers all of the values computed before.
@lru_cache(maxsize=None)
def nth_fibonacci_number(n: int) -> int:
    ''' Returns the nth Fibonacci number. '''
    if n <= 1:
        return n
    return nth_fibonacci_number(n-2) + nth_fibonacci_number(n-1)


if __name__ == '__main__':
    try:
        my_nth_number: int = int(input('Enter number: '))
    except ValueError:
        print('Value Error')
        sys.exit(1)

    print(f'{my_nth_number} Fibonacci number is: {nth_fibonacci_number(n=my_nth_number)}')
