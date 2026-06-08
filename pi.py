import math

def estimate_pi():
    sum = 0
    k = 0
    term = 1

    while term >= 1e-15:
        term = math.factorial(4*k) * (1103 + 26390*k) / (math.factorial(k)**4 * 396 ** (4*k))
        sum = sum + term
        k = k + 1

    return 9801 / (2*math.sqrt(2)) * 1 / sum

print(estimate_pi(), math.pi)
