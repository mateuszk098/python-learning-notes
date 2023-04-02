"""
See description at https://www.hackerrank.com/challenges/whats-your-name

You are given the firstname and lastname of a person on two different lines. 
Your task is to read them and print the following:

Hello firstname lastname! You just delved into python.
"""


def print_full_name(first: str, last: str) -> None:
    # Write your code here
    temp: str = f"Hello {first} {last}! You just delved into python."
    print(temp)


if __name__ == "__main__":
    first_name: str = input()
    last_name: str = input()
    print_full_name(first_name, last_name)
