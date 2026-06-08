def check_fermat(a, b, c, n):
    if (n > 2 and a**n + b**n == c**n):
        print("Holy smokes, Fermat was wrong!")

    print("No, that doesn't work.")

def try_fermat():
    a = input("Type the first number (a):\n")
    b = input("Type the second number (b):\n")
    c = input("Type the third number (c):\n")
    n = input("Type the power (n):")

    check_fermat(int(a), int(b), int(c), int(n))

try_fermat()
