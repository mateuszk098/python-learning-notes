"""
Simple palindrome checking algorithm.
A word, phrase, verse, or sentence that reads the same backward or forward.
"""


def is_palindrome(text):
    """Returns True if the text is a palindrome, otherwise returns False."""
    text_len = len(text)
    if text_len <= 1:
        return True

    index = 0
    # The '<' sign instead of '<=' because we don't have to check the middle letter.
    while index < text_len // 2:
        if text[index] != text[text_len - index - 1]:
            return False
        index += 1

    return True


assert is_palindrome("anana") == True
assert is_palindrome("banana") == False
assert is_palindrome("a") == True
assert is_palindrome("abba") == True
assert is_palindrome("tattarrattat") == True
assert is_palindrome("this is not a palindrome") == False
