"""
You are given n words. Some words may repeat. For each word, output
its number of occurrences. The output order should correspond with
the input order of appearance of the word. See the sample input/output
for clarification.

See description at https://www.hackerrank.com/challenges/word-order
"""


from collections import OrderedDict

n = int(input().strip())
words = OrderedDict()

for _ in range(n):
    word = input().strip()
    words[word] = words.get(word, 0) + 1

print(len(words))
for counts in words.values():
    print(counts, end=" ")
