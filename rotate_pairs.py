from rotated import rotate_word

def rotate_pairs(word, d):
    for i in range(1, 14):
        rotated = rotate_word(word, i)
        if rotated in d:
            print(word, i, rotated)

fin = open('words.txt')
word_dict = dict()

for line in fin:
    word = line.strip()
    word_dict[word] = None

for word in word_dict:
    rotate_pairs(word, word_dict)
