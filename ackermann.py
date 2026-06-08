def ack(m, n):
    if m == 0:
        return n + 1
    elif m > 0 and n == 0:
        return ack(m - 1, 1)
    elif m > 0 and n > 0:
        return ack(m - 1, ack(m, n - 1))

print(ack(3, 4))

memo = dict()

def mem_ack(m, n):
    if (str(m) + ", " + str(n)) in memo:
        return memo[str(m) + ", " + str(n)]

    if m == 0:
        memo[str(m) + ", " + str(n)] = n + 1
    elif m > 0 and n == 0:
        memo[str(m) + ", " + str(n)] = ack(m - 1, 1)
    elif m > 0 and n > 0:
        memo[str(m) + ", " + str(n)] = ack(m - 1, ack(m, n - 1))

    return memo[str(m) + ", " + str(n)]

print(mem_ack(3, 4))
