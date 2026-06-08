fin = open('words.txt')

def add_anagrams(word, wlt):
    letters = list(word)
    letters.sort()

    lettersKey = tuple(letters)

    wlt.setdefault(lettersKey, []).append(word)

def print_anagrams(wlt):
    for st in wlt:
        if len(wlt[st]) > 1:
            print(wlt[st])

def print_anagrams_length(wlt):
    t = []

    for st in wlt:
        t.append((len(wlt[st]), wlt[st]))

    t.sort(reverse=True)

    for length, words in t:
        if length > 1:
            print(words)

def bingos(wlt):
    t = []

    for st in wlt:
        if len(st) == 8:
            t.append((len(wlt[st]), st, wlt[st]))

    t.sort(reverse=True)
    maxLength = t[0][0]
    res = []

    for length, letters, words in t:
        if length == maxLength:
            res.append((letters, words))
        else:
            break

    return res

wordList = dict()

for line in fin:
    word = line.strip()
    add_anagrams(word, wordList)

# # print_anagrams(wordList)
# print_anagrams_length(wordList)

print(bingos(wordList))
