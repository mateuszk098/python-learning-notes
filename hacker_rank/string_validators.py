"""
See description at https://www.hackerrank.com/challenges/string-validators

You are given a string S.
Your task is to find out if the string S contains: alphanumeric characters, 
alphabetical characters, digits, lowercase and uppercase characters.
"""

if __name__ == "__main__":
    s = input()

    for action in ["isalnum()", "isalpha()", "isdigit()", "islower()", "isupper()"]:
        state = False
        for letter in s:
            if eval(f"letter.{action}"):
                state = True
                break
        print(state)
