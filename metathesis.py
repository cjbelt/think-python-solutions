from anagrams_tuples import add_anagrams

def find_metathesis(t):
    i = 0

    while i < len(t):
        j = i + 1

        while j < len(t):
            count = 0

            for letter1, letter2 in zip(t[i], t[j]):
                if letter1 != letter2:
                    count += 1

            if count == 2:
                print(t[i], t[j])

            j += 1

        i += 1

fin = open('words.txt')
anagrams = dict()

for line in fin:
    word = line.strip()
    add_anagrams(word, anagrams)

for sts in anagrams:
    find_metathesis(anagrams[sts])
