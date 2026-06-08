def make_translator(s):
    import string
    d = dict()
    puncts = string.punctuation

    for punct in puncts:
        d[punct] = None

    # d['-'] = '-'

    spaces = string.whitespace

    for space in spaces:
        d[space] = ' '

    for i in range(10):
        d[i] = None

    return s.maketrans(d)

def format_line(line):
    import string
    words = line.split(' ')

    for index, word in zip(range(len(words)), words):
        word = word.lower()
        translator = make_translator(word)
        words[index] = word.translate(translator).strip()

    return list(filter(lambda x: x != '', words))

def format_text(text):
    lines = []

    for line in text:
        words = format_line(line)

        if words != []:
            lines.append(words)

    return lines

def text_start(text):
    lines = format_text(text)

    for index, line in zip(range(len(lines)), lines):
        if len(line) > 0 and line[0] == 'start':
            return lines[index + 1:]

def total_words(text):
    count = 0

    for line in text:
        for word in line:
            count += 1

    return count

def word_frequency(text):
    wordCount = dict()

    for line in text:
        for word in line:
            wordCount[word] = wordCount.get(word, 0) + 1

    return wordCount

def diff_words(text):
    return len(word_frequency(text))

def most_frequents(counter, n):
    frequencies = list(zip(counter.values(), counter.keys()))
    frequencies.sort(reverse=True)
    tops = []

    for i in range(n):
        tops.append(frequencies[i])

    return tops

def different_words(dText, dWords):
    different_words = []

    for word in dText:
        if word not in dWords:
            different_words.append(word)

    return different_words

def subtract_sets(set1, set2):
    return set1 - set2

def cumulative_sum(d, keysT):
    sum = 0
    sumsT = []

    for key in keysT:
        sum += d[key]
        sumsT.append(sum)

    return sumsT

def bisect_range(t, value):
    min = 0
    max = len(t) - 1

    while min <= max:
        index = min + int((max-min+1) / 2) - (1 - (max-min+1) % 2)

        if t[index] == value:
            return index
        elif t[index] < value:
            min = index + 1
        else:
            max = index - 1

    return min

def random_word(d):
    import random
    keysList = list(d.keys())
    sums = cumulative_sum(d, keysList)
    randNum = random.randint(1, sums[len(sums) - 1])
    return keysList[bisect_range(sums, randNum)]

# fin = open('loremipsum.txt')

# print(format_text(fin))

# fin = open('moby.txt')
# print(format_text(fin)[:30])
# formated_fin = text_start(fin)

# print("Total Words: ", total_words(formated_fin))
# print("Different words: ", diff_words(formated_fin))


# top20Words = most_frequents(word_frequency(formated_fin), 20)

# for freq, word in top20Words:
#     print(word, ": ", freq, " times")

# words = open('words.txt')
# wordDictionary = dict()

# for line in words:
#     word = line.strip()
#     wordDictionary[word] = True

# print(different_words(word_frequency(formated_fin), wordDictionary))
# print(subtract_sets(set(word_frequency(formated_fin).keys()), set(wordDictionary.keys())))

# hist = word_frequency(formated_fin)

# for i in range(20):
#     print(random_word(hist))
