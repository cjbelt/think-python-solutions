def rotate_word(word, n):
    if len(word) == 0:
        return ''

    start = 0

    if word[0].isupper():
        start = 65
    elif word[0].islower():
        start = 97

    num = ((ord(word[0]) - start + n) % 26) + start
    newWord = chr(num) + rotate_word(word[1:], n)
    return newWord

print(rotate_word("melon", -10))
print(rotate_word('MELON', -10))
