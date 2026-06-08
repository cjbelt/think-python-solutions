from slice_palindrome import is_palindrome

i = 100000

while i < 1000000:
    if (is_palindrome(str(i)[2:]) and is_palindrome(str(i+1)[1:])
     and is_palindrome(str(i+2)[1:5]) and is_palindrome(str(i+3))):
        print(i)

    i = i + 1
