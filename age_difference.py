def is_reverse(n1, n2):
    return str(n2).zfill(2) == str(n1).zfill(2)[::-1]

def search_reverses(difference):
    count = 0
    n1 = 1
    n2 = n1 + difference
    n6 = 0

    while n2 < 120:
        if is_reverse(n1, n2):
            count = count + 1

            if count == 6:
                n6 = n1

        n1 = n1 + 1
        n2 = n2 + 1

    if count == 8:
        print(n6)

    return count

d = 10

while d < 60:
    search_reverses(d)
    d = d + 1
