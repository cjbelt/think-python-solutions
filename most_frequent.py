def most_frequent(s):
    freq = dict()

    for letter in s:
        key = letter.lower()
        freq[key] = freq.get(key, 0) + 1

    t = []

    for letter in freq:
        t.append((freq[letter], letter))

    t.sort(reverse=True)

    for f, letter in t:
        print(letter, f)

engText = "We hold these truths to be self-evident, that all men are created equal, that they are endowed by their Creator with certain unalienable Rights, that among these are Life, Liberty and the pursuit of Happiness."

print(most_frequent(engText))
