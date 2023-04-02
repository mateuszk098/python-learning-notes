"""
See description at https://www.hackerrank.com/challenges/merge-the-tools/problem
"""


def merge_the_tools(string, k):
    # your code goes here
    sequences = [string[i:i+k] for i in range(0, len(string), k)]
    results = []

    for seq in sequences:
        tmp = list(seq)
        tmp = list(dict.fromkeys((tmp)))  # Works like an "ordered" set.
        results.append("".join(tmp))

    print(*results, sep="\n")


if __name__ == "__main__":
    string, k = input(), int(input())
    merge_the_tools(string, k)
