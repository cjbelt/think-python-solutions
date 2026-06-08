def is_power(a, b):
    if a == b:
        return True
    elif a % b != 0:
        return False

    return is_power(a/b, b)

print(is_power(18, 6))
