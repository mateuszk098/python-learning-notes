"""
You are given a string S. S contains alphanumeric characters only.
Your task is to sort the string S in the following manner:

* All sorted lowercase letters are ahead of uppercase letters.
* All sorted uppercase letters are ahead of digits.
* All sorted odd digits are ahead of sorted even digits.

See description at https://www.hackerrank.com/challenges/ginorts
"""


s = input()
l = list(s)

low = sorted(char for char in l if char.islower())
up = sorted(char for char in l if char.isupper())
odd = sorted(char for char in l if char.isdigit() and int(char) % 2 != 0)
even = sorted(char for char in l if char.isdigit() and int(char) % 2 == 0)

new_s = "".join(low) + "".join(up) + "".join(odd) + "".join(even)
print(new_s)
