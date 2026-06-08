import dicts

def choose_from_hist(hist):
    import random
    t = []

    for word in hist:
        t.extend([word] * hist[word])

    return random.choice(t)

hist = {'a': 99, 'b': 1}

for i in range(100):
    print(choose_from_hist(hist))
