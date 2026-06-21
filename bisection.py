import math

def find_middle(t):
    if len(t) % 2 == 0:
        i = len(t) / 2 - 1
        j = i + 1
        return (t[i] + t[j]) / 2
    else:
        i = math.floor(len(t) / 2)
        return t[i]

def bisection_search(t, item):
    middle_i = math.floor(len(t) / 2)

    if item == t[middle_i]:
        return middle_i
    elif item < t[middle_i]:
        return bisection_search(t[:middle_i], item)
    elif item > t[middle_i]:
        return middle_i + 1 + bisection_search(t[middle_i + 1:], item)
    else:
        return None

def bisection_search_2(t, item):
    start = 0
    end = len(t) - 1

    while start <= end:
        middle = start + math.floor((end - start + 1)/2) - (1 - (end - start + 1)%2)

        if item == t[middle]:
            return middle
        elif item < t[middle]:
            end = middle - 1
        elif item > t[middle]:
            start = middle + 1

    return None


if __name__ == '__main__':
    t = [0, 3, 9, 15, 103, 235, 567, 1036]
    print(bisection_search(t, 103))
    print(bisection_search_2(t, 102))
