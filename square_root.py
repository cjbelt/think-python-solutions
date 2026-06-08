def square_root(a):
    x = a / 2
    while True:
        y = (x + a/x) / 2

        if abs(y - x) < 0.0000001:
            return y

        x = y

# square_root(16)

def test_square_root():
    import math
    x = 1.0

    while x < 10:
        r1 = square_root(x)
        r2 = math.sqrt(x)
        print(x, ' ', r1, ' ' * 5, r2, ' ' * 5, abs(r1 - r2))
        x = x + 1

test_square_root()
