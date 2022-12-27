"""
Example implementation of Knuth-Morris-Pratt searching.

Time complexity: O(n+m), where n is the length of the text string
and m is the length of the pattern string.

Space complexity: O(m), because it uses an array to store the shift values
for the pattern string.
"""


def knuth_morris_pratt(pattern, text):
    """Knuth-Morris-Pratt algorithm of pattern searching."""

    # Initialize the shift array
    shift = _init_shift(pattern)

    # Initialize variables for traversing the strings
    pattern_index = 0
    text_index = 0

    # Get the length of the pattern and text strings
    pattern_length = len(pattern)
    text_length = len(text)

    # Iterate through the strings until either the pattern or text is exhausted
    while text_index < text_length and pattern_index < pattern_length:
        # If the characters at the current indices do not match,
        # reset the pattern index using the shift array
        while pattern_index >= 0 and text[text_index] != pattern[pattern_index]:
            pattern_index = shift[pattern_index]

        # Move to the next character in both strings
        text_index += 1
        pattern_index += 1

    # If the pattern has been fully traversed,
    # return the starting index of the pattern in the text
    if pattern_index == pattern_length:
        return text_index - pattern_length

    # If the pattern was not found, return -1
    return -1


def _init_shift(pattern):
    # Initialize the shift array
    pattern_length = len(pattern)
    shift = [0] * pattern_length
    shift[0] = -1

    # Initialize variables for traversing the pattern string
    pattern_index = 0
    shift_index = -1

    # Iterate through the pattern until the second-to-last character
    while pattern_index < pattern_length - 1:
        # Update the shift array using the previous value
        shift[pattern_index] = shift_index
        # If the characters at the current indices do not match,
        # reset the shift index using the shift array
        while shift_index >= 0 and pattern[pattern_index] != pattern[shift_index]:
            shift_index = shift[shift_index]
        # Move to the next character in both the pattern and shift arrays
        pattern_index += 1
        shift_index += 1

    # Return the shift array
    return shift


assert knuth_morris_pratt("ris", "knuth morris pratt") == 9  # pattern in middle of text
assert knuth_morris_pratt("def", "abcdef") == 3  # pattern at end of text
assert knuth_morris_pratt("efg", "abcdef") == -1  # pattern not in text
assert knuth_morris_pratt("ab", "aabcdef") == 1  # pattern not at start of text
assert knuth_morris_pratt("cd", "abcdef") == 2  # pattern in middle of text
assert knuth_morris_pratt("abc", "abcabc") == 0  # pattern repeated in text
assert knuth_morris_pratt("a", "aaaaaa") == 0  # pattern of all the same character
assert knuth_morris_pratt("aaa", "baaaaa") == 1  # pattern of all the same character, not at start of text
assert knuth_morris_pratt("ananas", "ananasa") == 0
