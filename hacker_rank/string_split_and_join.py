"""
See description at https://www.hackerrank.com/challenges/python-string-split-and-join

You are given a string. Split the string on a " " (space) delimiter 
and join using a - hyphen.
"""


def split_and_join(line: str) -> str:
    # write your code here
    modified_line: list = line.split(" ")
    return "-".join(modified_line)


if __name__ == "__main__":
    my_line: str = input()
    result: str = split_and_join(my_line)
    print(result)
