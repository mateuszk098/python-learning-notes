"""
Example implementation of Boyer-Moore searching.

Time complexity: O(n/m), where n is the length of the text and m is the
length of the pattern.

Space complexity: O(1), since it only uses a fixed amount of memory regardless
of the size of the input.
"""


def boyer_moore(pattern, text):
    """Searches for the pattern in the text using the Boyer-Moore algorithm.

    Returns the position at which the pattern is found in the text,
    or -1 if the pattern is not found.
    """

    # Preprocess the pattern to generate the jump table
    jump_table = {}
    pattern_length = len(pattern)
    for i in range(pattern_length - 1):
        jump_table[pattern[i]] = pattern_length - i - 1

    # Search for the pattern in the text
    text_length = len(text)
    text_index = pattern_length - 1
    while text_index < text_length:
        pattern_index = pattern_length - 1
        while pattern_index >= 0 and text[text_index] == pattern[pattern_index]:
            text_index -= 1
            pattern_index -= 1
        if pattern_index == -1:
            # Pattern found at position text_index + 1
            return text_index + 1

        # Get the jump distance from the jump table
        jump = jump_table.get(text[text_index], pattern_length)

        # Shift the pattern by the jump distance
        text_index += jump

    # Pattern not found
    return -1


assert boyer_moore("abc", "abcdef") == 0  # pattern at start of text
assert boyer_moore("def", "abcdef") == 3  # pattern at end of text
assert boyer_moore("efg", "abcdef") == -1  # pattern not in text
assert boyer_moore("abc", "aabcdef") == 1  # pattern not at start of text
assert boyer_moore("bcd", "abcdef") == 1  # pattern in middle of text
assert boyer_moore("", "abcdef") == 0  # empty pattern
assert boyer_moore("abc", "") == -1  # empty text
assert boyer_moore("abc", "abcabc") == 0  # pattern repeated in text
assert boyer_moore("aaa", "aaaaaa") == 0  # pattern of all the same character
assert boyer_moore("aaa", "baaaaa") == 1  # pattern of all the same character, not at start of text
