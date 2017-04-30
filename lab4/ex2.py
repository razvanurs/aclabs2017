#! python3
import re


def word_count(word, path):
    wc = 0
    with open(path, 'r') as fp:
        for line in fp:
            wc += sum(1 for w in re.sub("[^\w]", " ",  line).split() if word.lower() == w.lower())
    return wc

print(word_count('love', 'pg100.txt'))
