def has_duplicates(t):
    count = dict()

    for word in t:
        if word in count:
            return True

        count[word] = True

    return False

t = [1, 2, 3, 4, 4, 5]
print(has_duplicates(t))
