from app import text_model
from utils import math_tools
from utils.text_tools import sentences


def main():
    sen = ["This is a sentence", "This is another sentence"]
    for sentence in text_model.create_sentences(sen):
        print(sentence)
        print("Mean word length:", sentence.mean_word_len())

    s1 = sentences.Sentence("Ad alias quae aliquam in ea nisi.")
    for s in s1:
        print(s)


if __name__ == "__main__":
    main()
