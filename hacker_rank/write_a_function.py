"""
See description at https://www.hackerrank.com/challenges/write-a-function

Given a year, determine whether it is a leap year. If it is a leap year, 
return the Boolean True, otherwise return False.

Note that the code stub provided reads from STDIN and passes arguments 
to the is_leap function. It is only necessary to complete the is_leap function.
"""


def is_leap(year: int) -> bool:
    leap: bool = False

    # Write your logic here
    if year % 4 == 0:
        leap = True
    if year % 100 == 0:
        leap = False
    if year % 400 == 0:
        leap = True

    return leap


if __name__ == "__main__":
    my_year = int(input())
    print(is_leap(my_year))
