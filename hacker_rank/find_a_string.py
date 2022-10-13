def count_substring(sentence: str, sub_sentence: str) -> int:

    counter: int = 0

    for index in range(len(sentence)):
        if sentence[index:].startswith(sub_sentence):
            counter += 1

    return counter


if __name__ == '__main__':
    sen: str = input().strip()
    sub_sen: str = input().strip()
    count: int = count_substring(sen, sub_sen)
    print(count)
