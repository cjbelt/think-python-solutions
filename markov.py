import structure_selection
import random

def markov_analysis(text, length=2):
    dictionary = dict()
    i = 0
    lines = structure_selection.text_start(text)
    prefix = ()

    for line in lines:
        for word in line:
            if len(prefix) < length:
                prefix += (word, )
                continue

            dictionary.setdefault(prefix, [])
            dictionary[prefix].append(word)
            prefix = prefix[1:] + (word, )

    return dictionary

def choose_words(text, prefix_len=2, new_text_len=20):
    markov = markov_analysis(text, prefix_len)
    prefixes = list(markov.keys())
    s = ''
    prefix = random.choice(prefixes)

    for i in range(new_text_len):
        while markov.get(prefix, []) == []:
            prefix = random.choice(prefixes)

        word = random.choice(markov[prefix])
        s += word + ' '
        prefix = prefix[1:] + (word, )

    return s

# fin = open('moby.txt')
# print(choose_words(fin, 5))
