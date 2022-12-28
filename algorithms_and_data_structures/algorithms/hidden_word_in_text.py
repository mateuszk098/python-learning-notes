"""
Check if the given sentence contains given word.
"""


def is_hidden_word_in_text(text, word):
    """Return True if the given text contains a hidden word, otherwise return False."""
    word_len, text_len = len(word), len(text)
    if word_len > text_len:
        return False

    text_lst = list(text)
    for letter in word:  # One should have as many removes as there are letters in word.
        try:
            text_lst.remove(letter)
        except ValueError:
            return False

    return True


assert is_hidden_word_in_text("the cheetah jumps over the lazy dog", "crazy") == True
assert is_hidden_word_in_text("the cheetah jumps over the lazy dog", "false") == False
assert is_hidden_word_in_text("banana", "ana") == True
