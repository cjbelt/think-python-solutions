fin = open('words.txt')
# for line in fin:
#     word = line.strip()
#     if len(word) > 20:
#         print(word)

def has_no_e(word):
    for c in word:
        if c.lower() == 'e':
            return False

    return True

def avoids(word, letters):
    for letter1 in word:
        for letter2 in letters:
            if letter1.lower() == letter2.lower():
                return False

    return True

def uses_only(word, letters):
    for letter1 in word:
        isEqual = False

        for letter2 in letters:
            if letter1.lower() == letter2.lower():
                isEqual = True
                break

        if not isEqual:
            return False

    return True

def uses_all(word, letters):
    for letter1 in letters:
        isEqual = False

        for letter2 in word:
            if letter1.lower() == letter2.lower():
                isEqual = True
                break

        if not isEqual:
            return False

    return True

def is_abecedarian(word):
    num = ord(word[0].lower())
    for letter in word:
        if ord(letter.lower()) < num:
            return False

    return True

def three_double(word):
    count = 0
    i = 1
    while i < len(word):
        if word[i] == word[i - 1]:
            count = count + 1
            i = i + 1
        elif count == 3:
            return True
        else:
            count = 0

        i = i + 1

    return False



# count = 0
# for line in fin:
#     word = line.strip()
#     if has_no_e(word):
#         print(word)
#         count = count + 1

# print("Percentage: ", count / 113809, "%")

# forbidden = input("Write a string of forbidden letters:")
# count = 0
# for line in fin:
#     word = line.strip()
#     if avoids(word, forbidden):
#         count = count + 1

# print(count)

# for line in fin:
#     word = line.strip()
#     if uses_only(word, 'acefhlo'):
#         print(word)

# for line in fin:
#     word = line.strip()
#     if uses_all(word, 'aeiouy'):
#         print(word)

# for line in fin:
#     word = line.strip()
#     if is_abecedarian(word):
#         print(word)

for line in fin:
    word = line.strip()
    if three_double(word):
        print(word)
