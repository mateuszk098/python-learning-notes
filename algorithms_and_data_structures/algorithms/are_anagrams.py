"""
Simple anagram checking algorithm.
A word or phrase formed by reordering the letters of another word or phrase.
"""

from collections import defaultdict

# def are_anagrams(text1, text2):
#     """Returns True if texts are anagrams, otherwise returns False."""
#     if len(text1) != len(text2):
#         return False

#     s1 = [letter for letter in text1 if letter != " "]
#     s2 = [letter for letter in text2 if letter != " "]

#     return sorted(s1) == sorted(s2)


def are_anagrams(text1, text2):
    """Returns True if texts are anagrams, otherwise returns False."""
    if len(text1) != len(text2):
        return False

    d1 = defaultdict(int)
    d2 = defaultdict(int)

    for letter in text1:
        d1[letter] += 1

    for letter in text2:
        d2[letter] += 1

    return d1 == d2


assert are_anagrams("angel", "glean") == True
assert are_anagrams("state", "taste") == True
assert are_anagrams("a gentleman", "elegant man") == True
assert are_anagrams("eleven plus two", "twelve plus one") == True
assert are_anagrams("there are", "not anagrams") == False
assert are_anagrams("", "not") == False
