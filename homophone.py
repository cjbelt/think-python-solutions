from pronounce import read_dictionary

def make_wordlist():
    fin = open('words.txt')
    wordlist = dict()

    for line in fin:
        word = line.strip()
        wordlist[word] = None

    return wordlist

dictionary = make_wordlist()
pronounce_list = read_dictionary('c06d.txt')

def homophone(word, p):
    word2 = word[1:]
    word3 = word[0] + word[2:]

    if len(word) == 5 and word in p and word2 in p and word3 in p:
        return (p[word] == p[word2]) and (p[word] == p[word3])

for word in dictionary:
    if homophone(word, pronounce_list):
        print(word, word[1:], word[0] + word[2:])
