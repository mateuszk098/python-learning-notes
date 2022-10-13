'''
Simple text analysis.
Go here -> https://gutenberg.org/
'''


def analyse_book(fname: str, word: str) -> None:
    ''' Prints how many times "word" appears in the book. '''
    try:
        with open(file=fname, mode='r', encoding='utf-8') as f:
            content: str = f.read()
    except FileNotFoundError:
        print('File not found!')
    else:
        words: list[str] = content.lower().split()
        words_number: int = len(words)
        word_number: int = content.count(word)
        sentence: str = f"This book has {words_number} words.\n"\
            f"The word '{word}' occurs {word_number} times, "\
            f"which is {word_number/words_number*100:.2f}%."
        print(sentence)


def main() -> None:
    ''' Main function. '''
    filename: str = input('Enter filename: ')
    my_word: str = input('Enter a word: ')
    analyse_book(fname=filename, word=my_word)


if __name__ == '__main__':
    main()
