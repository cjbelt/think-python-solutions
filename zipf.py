import string
import math

hist = {}

def skip_start(text):
    for line in text:
        if line.startswith("*** START OF"):
            return

def process_text(text, hist):
    fin = open(text)
    skip_start(fin)

    for line in fin:
        process_line(line, hist)

        if line.startswith("*** END OF"):
            break

    return hist

def process_line(line, hist):
    line = line.replace('-', ' ')
    strippables = string.whitespace + string.punctuation

    for word in line.split():
        word = word.strip(strippables).lower()
        hist[word] = hist.get(word, 0) + 1

def rank_words_frequencies(hist):
    ranks = []

    for key, value in hist.items():
        ranks.append((value, key))

    ranks.sort(reverse=True)
    return zip(range(1, len(ranks)), ranks)

def print_rank(text, hist):
    hist = process_text(text, hist)
    for r, (f, word) in rank_words_frequencies(hist):
        print(word, math.log10(r), math.log10(f))

def draw_graph(text, hist):
    import matplotlib.pyplot as plt
    import numpy as np
    r_values = []
    f_values = []
    process_text(text, hist)
    ranks = rank_words_frequencies(hist)

    for r, (f, word) in ranks:
        r_values.append(r)
        f_values.append(f)

    fig, ax = plt.subplots()
    ax.plot(r_values, f_values)
    plt.show()

# print_rank('moby.txt')

# draw_graph('moby.txt', hist)
