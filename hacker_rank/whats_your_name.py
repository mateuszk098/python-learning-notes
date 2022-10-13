#
# Complete the 'print_full_name' function below.
#
# The function is expected to return a STRING.
# The function accepts following parameters:
#  1. STRING first
#  2. STRING last
#

def print_full_name(first: str, last: str) -> None:
    # Write your code here
    temp: str = f"Hello {first} {last}! You just delved into python."
    print(temp)

if __name__ == '__main__':
    first_name: str = input()
    last_name: str = input()
    print_full_name(first_name, last_name)
