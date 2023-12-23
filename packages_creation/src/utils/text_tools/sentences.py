from ..math_tools import operations


class Sentence:
    def __init__(self, sentence):
        self.sentence = sentence
        self.words = self.sentence.split()

    def __iter__(self):
        for word in self.words:
            yield word

    def __len__(self):
        return len(self.words)

    def __getitem__(self, index):
        return self.words[index]

    def __repr__(self):
        return f"{type(self).__name__}({self.sentence!r})"

    def mean_word_len(self):
        return operations.my_quot(len(self.sentence), len(self.words))

    @classmethod
    def from_file(cls, file_path: str):
        with open(file_path, "r") as f:
            return cls(f.read())
