def histogram(s):
    d = dict()
    for c in s:
        d[c] = d.get(c, 0) + 1

    return d

def print_hist(h):
    lt = list(h.keys())
    lt.sort()

    for c in lt:
        print(c, h[c])

def reverse_lookup(d, v):
    s = []

    for k in d:
        if d[k] == v:
            s.append(k)

    return s

def invert_dict(d):
    inverse = dict()

    for key in d:
        val = inverse.setdefault(d[key], [])
        val.append(key)

    return inverse

# h = histogram('parrot')
# print_hist(h)
# print(reverse_lookup(h, 3))
# print(invert_dict(h))
