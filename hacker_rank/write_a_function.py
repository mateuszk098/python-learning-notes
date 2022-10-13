def is_leap(year: int) -> bool:
    leap: bool = False

    # Write your logic here
    if year > 1900 or year < 10000:
        if year % 4 == 0:
            leap = True
            if year % 100 == 0:
                leap = False
                if year % 400 == 0:
                    leap = True

    return leap


if __name__ == '__main__':
    my_year = int(input())
    print(is_leap(my_year))
