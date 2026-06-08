def sumall(*nums):
    sum = 0

    for num in nums:
        sum += num

    return sum

# print(sumall(1, 2, 3))

from random import random

def sort_by_length(words):
    t = []
    for word in words:
        t.append((len(word), random(), word))

    t.sort(reverse=True)

    res = []
    for length, num, word in t:
        res.append(word)

    return res

print(sort_by_length(['abc', 'water', 'watermelon', 'black']))
