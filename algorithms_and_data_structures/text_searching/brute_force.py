"""
Example implementation of Brute Force searching.

Time complexity: O(n*m), where n is the length of the text string
and m is the length of the pattern string.

Space complexity: O(1), because it only uses a constant amount
of memory regardless of the size of the input.
"""


def brute_force(pattern, text):
    """Brute force algorithm of pattern searching."""

    # Initialize variables for traversing the strings.
    pattern_index = 0
    text_index = 0

    # Get the length of the pattern and text strings.
    pattern_length = len(pattern)
    text_length = len(text)

    # Iterate through the strings until either the pattern or text is exhausted.
    while pattern_index < pattern_length and text_index < text_length:
        # If the characters at the current indices do not match,
        # reset the pattern index and move the text index back.
        if text[text_index] != pattern[pattern_index]:
            text_index -= pattern_index
            pattern_index = -1

        # Move to the next character in both strings.
        text_index += 1
        pattern_index += 1

    # If the pattern has been fully traversed, return the starting index
    # of the pattern in the text.
    if pattern_index == pattern_length:
        return text_index - pattern_length

    # If the pattern was not found, return -1
    return -1


assert brute_force("abc", "abcdef") == 0  # pattern at start of text
assert brute_force("def", "abcdef") == 3  # pattern at end of text
assert brute_force("efg", "abcdef") == -1  # pattern not in text
assert brute_force("abc", "aabcdef") == 1  # pattern not at start of text
assert brute_force("bcd", "abcdef") == 1  # pattern in middle of text
assert brute_force("", "abcdef") == 0  # empty pattern
assert brute_force("abc", "") == -1  # empty text
assert brute_force("abc", "abcabc") == 0  # pattern repeated in text
assert brute_force("aaa", "aaaaaa") == 0  # pattern of all the same character
assert brute_force("aaa", "baaaaa") == 1  # pattern of all the same character, not at start of text
