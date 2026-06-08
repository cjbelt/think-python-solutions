memo = dict()
memo[(0, '')] = ['']

def word_childrens(word, wordDict):
    t = []
    wordT = list(word)


    for index, letter in zip(range(len(wordT)), wordT):
        wordTCp = wordT.copy()
        del wordTCp[index]
        wordCp = ''.join(wordTCp)

        if wordDict.get(wordCp, False) == True:
            t.append(wordCp)

    return t

def reducible_word(word, wordDict):
    if (len(word), word) in memo:
        return memo[(len(word), word)]

    children = word_childrens(word, wordDict)
    t = []

    for child in children:
        if reducible_word(child, wordDict):
            t.append(child)

    memo[(len(word), word)] = t
    return t

wordDict = {'i': True, 'a': True, '': True}
fin = open('words.txt')

for line in fin:
    word = line.strip()
    wordDict[word] = True

# for word in wordDict:
#     if reducible_word(word, wordDict) == True:
#         print(word)

for word in wordDict:
    reducible_word(word, wordDict)

ltMemo = list(memo.keys())
ltMemo.sort(reverse=True)
count = 0

for length, word in ltMemo:
    if memo[(length, word)] != []:
        print(word)
        count += 1

    if count == 5:
        break
