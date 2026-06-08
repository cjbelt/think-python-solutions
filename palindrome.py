def first(word):
    return word[0]

def last(word):
    return word[-1]

def middle(word):
    return word[1:-1]

# print(first("long"), last("long"), middle("long"), middle("eight"))

def is_palindrome(word):
    if len(word) == 1:
        return True
    elif first(word) != last(word):
        return False

    return is_palindrome(middle(word))

print(is_palindrome("redivider"))
print(is_palindrome("bitch"))
