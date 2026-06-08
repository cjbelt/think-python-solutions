import random

def has_duplicates(t):
    for i in range(len(t)):
        j = i + 1
        while j < len(t):
            if t[i] == t[j]:
                return True
            j += 1

    return False

samples = []
count = 0
n = 1000
students = 23

for i in range(n):
    samples.append([])
    for j in range(students):
        samples[i].append(random.randint(1, 365))

    if has_duplicates(samples[i]):
        count = count + 1

print(count / n * 100, "%")
