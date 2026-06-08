def is_sorted(t):
    for i in range(len(t) - 1):
        if t[i] > t[i + 1]:
            return False

    return True

# print(is_sorted([1, 2, 2]))
# print(is_sorted(['b', 'a']))

def is_anagram(s1, s2):
    t1 = list(s1)
    t2 = list(s2)
    t1.sort()
    t2.sort()
    t1 = ''.join(t1)
    t2 = ''.join(t2)

    if len(t1) == len(t2):
        for i in range(len(t1)):
            if t1[i] != t2[i]:
                return False
    else:
        return False

    return True

# print(is_anagram("night", "thing"))
# print(is_anagram("sick", "budget"))

def remove_duplicates(t):
    s = t[:]
    s.sort()
    i = 0
    rang = len(s) - 1

    while i < rang:
        if s[i] == s[i+1]:
            del s[i]
            del s[i]
            rang -= 2
            i -= 1

        i += 1

    return s

# t = [1, 2, 3, 4, 5, 1, 7, 8, 7]
# print(remove_duplicates(t))

def word_list_append():
    fin = open("words.txt")
    arr = []

    for line in fin:
        word = line.strip()
        arr.append(word)

    return arr

def word_list_sum():
    fin = open("words.txt")
    arr = []

    for line in fin:
        word = line.strip()
        arr = arr + [word]

    return arr

# print(word_list_sum())

def bisect(t, word):
    min = 0
    max = len(t) - 1

    while min <= max:
        index = min + (int((max-min+1) / 2) - (1 - (max-min+1) % 2)) # if even, - 1; if odd, - 0
        if t[index] == word:
            return index
        elif t[index] > word:
            max = index - 1
        else:
            min = index + 1

    return None

# t = word_list_append()

# print(bisect(t, "cucumber"))
# print(bisect(t, "lambisgoia"))
# print(bisect(t, "zebra"))
# print(bisect(t, "lost"))

def reverse_pair(t):
    for i in range(len(t)):
        reversed = t[i][::-1]
        reversedIndex = bisect(t, reversed)
        if reversedIndex and reversedIndex > i:
            print(t[i], reversed)

# reverse_pair(t)

def interlocks(t):
    for i in range(len(t)):
        word1 = t[i][::2]
        word2 = t[i][1::2]

        if bisect(t, word1) and bisect(t, word2):
            print(word1, word2)

# print(interlocks(t))

def interlock_general(t, word, n = 3):
    for i in range(n):
        if not bisect(t, word[i::n]):
            return False

    return True

# for word in t:
#     if interlock_general(t, word, 3):
#         print(word)
