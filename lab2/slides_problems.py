#!python3
from collections import OrderedDict
from itertools import combinations


#  1 - invert a given list
def invert(int_list):
    return [-x for x in int_list]


# 2 - count occurrences of a word in a given string
def count(string):
    counter = dict()
    for word in string.split():
        if word in counter:
            counter[word] += 1
        else:
            counter[word] = 1

    return OrderedDict(sorted(counter.items()))


# 3 - flatten a list
def _flatten(int_list, depth, partial_result):
    if depth == 0:
        return int_list

    for item in int_list:
        if type(item) is list:
            # extend the initial list with element list
            partial_result.extend(item)
        else:
            partial_result.append(item)
    return _flatten(partial_result, depth - 1, [])


def flatten(int_list, depth):
    return _flatten(int_list, depth, [])


# 4 all subsets from list
def generate(int_list):
    result = []
    stop = len(int_list) + 1
    for i in range(0, stop):
        for item in combinations(int_list, i):
            result.append(set(item))
    return result


# 1
print('-' * 30)
l = [1, 2, 3, 4, 5]
print('initial: {}'.format(l))
print('inverted: {}\n'.format(invert(l)))

# 2
print('-' * 30)
test_string = 'albatross are blue and blue'
occurrences = count(test_string)
for k in occurrences:
    print(k, occurrences[k])

# 3
print('-' * 30)
print(flatten([1, 2], 1))
print(flatten([1, 2, [3]], 1))
print(flatten([1, 2, [3, [4]]], 2))

# 4
print(generate([1, 2, 3]))
