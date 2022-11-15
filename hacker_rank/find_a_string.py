"""
See secription at https://www.hackerrank.com/challenges/find-a-string

In this challenge, the user enters a string and a substring. You have to print 
the number of times that the substring occurs in the given string. String 
traversal will take place from left to right, not from right to left.

NOTE: String letters are case-sensitive.
"""


def count_substring(sentence: str, sub_sentence: str) -> int:
    counter: int = 0

    for index in range(len(sentence)):
        if sentence[index:].startswith(sub_sentence):
            counter += 1

    return counter


if __name__ == "__main__":
    sen: str = input().strip()
    sub_sen: str = input().strip()
    count: int = count_substring(sen, sub_sen)
    print(count)
