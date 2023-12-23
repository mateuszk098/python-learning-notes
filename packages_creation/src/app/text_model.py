from utils.text_tools import sentences


def create_sentences(sentences_list):
    for sentence in sentences_list:
        yield sentences.Sentence(sentence)
