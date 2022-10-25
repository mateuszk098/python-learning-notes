'''
Creates histogram of most common words in "Pan Tadeusz"
Usage: python lab01.py pan-tadeusz-pl.txt n m
where n - n most common words, m -  with at least m letters.
'''

import sys
import os.path
import codecs
from collections import Counter

from matplotlib import pyplot as plt
from matplotlib.pyplot import figure


def words_in_book(file_name: str, how_many_words: int, word_min_len: int, ignored: list) -> None:

    print(f"You get a histogram of the {how_many_words} most frequent words")
    print(f"where a word has at least {word_min_len} letters.")

    with codecs.open(file_name, 'r', 'utf-8') as file:
        word_list: list[str] = [word.lower() for line in file for word in line.split()
                                if (len(word) >= word_min_len and word.isalpha())]

    word_counter: Counter[str] = Counter(word_list)

    # Discard ignored words.
    if ignored:
        for word in ignored:
            if word in word_counter:
                print(f"You ignore word: '{word}'.")
                print(f"This word has got {word_counter[word]} counts.")
                del word_counter[word]

    if word_counter.most_common(how_many_words):
        word, popularity = zip(*word_counter.most_common(how_many_words))
        word, popularity = list(word), list(popularity)  # type: ignore
    else:
        print("Looks like there are not such long words.")
        sys.exit(0)

    # Most common at the top.
    popularity.reverse()  # type: ignore
    word.reverse()

    plt.style.use("seaborn")
    figure(figsize=(8, 4.5), dpi=100)
    plt.barh(word, popularity, height=0.7)

    # Values at poles.
    for index, value in enumerate(popularity):
        plt.text(int(value), index - 0.05, str(value), color='white', va="center",
                 ha="right", fontweight='bold', fontname="Times New Roman", fontsize=12)

    plt.title("\"Pan Tadeusz\" - Most Common Words", fontname="Times New Roman", fontsize=14)
    plt.xlabel("Number of counts", fontname="Times New Roman", fontsize=12)
    plt.show()


if __name__ == '__main__':

    # Ignoring words
    ignore_words: list[str] = ['lecz', 'jest']
    file_name: str = str(sys.argv[1])

    if not os.path.isfile(file_name):
        print("File not found. Try one more time.")
        sys.exit(0)

    try:
        how_many_words: int = int(sys.argv[2])
        word_min_len: int = int(sys.argv[3])
    except ValueError:
        print("Error value. Try one more time.")
        sys.exit(0)

    if how_many_words > 0 and word_min_len >= 0:
        words_in_book(file_name, how_many_words, word_min_len, ignore_words)
    else:
        print("Why do you want to use such strange values? Try one more time.")
        sys.exit(0)
