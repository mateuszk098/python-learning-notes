"""
See description at https://www.hackerrank.com/challenges/the-minion-game

Why this works?
Notice that
A player gets +1 point for each occurrence of the substring in the string.

From BANANA, We choose:
6 words started with B are B, BA, BAN, BANA, BANAN, BANANA
5 words with A are A, AN, ANA, ANAN, ANANA
4 words with N are N, NA, NAN, NANA
3 words with A are A, AN, ANA
2 words with N are N, NA
1 word with A is A
So e.g. for Stuart we have 6 words + 4 words + 2 words = 12 words.
"""


def minion_game(string):
    # your code goes here
    vowels = "AEIOU"
    kevin_result, stuart_result = 0, 0

    for index, letter in enumerate(string):
        if letter in vowels:
            kevin_result += len(string) - index
        else:
            stuart_result += len(string) - index

    if kevin_result > stuart_result:
        print("Kevin", kevin_result)
    elif kevin_result < stuart_result:
        print("Stuart", stuart_result)
    else:
        print("Draw")


if __name__ == "__main__":
    s = input()
    minion_game(s)
