"""
Given a string s, which is the company name in lowercase letters,
your task is to find the top three most common characters in the string.

* Print the three most common characters along with their occurrence count.
* Sort in descending order of occurrence count.
* If the occurrence count is the same, sort the characters in alphabetical order.

See description at https://www.hackerrank.com/challenges/most-commons
"""

from collections import Counter

if __name__ == '__main__':
    s = input().strip()

    stmp = sorted(s)
    cnt = Counter(stmp)
    top3 = cnt.most_common(3)

    for (letter, counts) in top3:
        print(letter, counts)
