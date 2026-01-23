'''
A palindrome Is a sequence of characters that reads the same forward and backward.
Given a string. determine if it's a palindrome after removing all non-alphanumeric charac·
ters. A character is alphanumeric if it's either a letter or a number
'''


def check_palindrome(s: str):
    left = 0
    right = len(s) - 1
    while left < right:
        while left < right and not s[left].isalnum():
            left += 1
        while left < right and not s[right].isalnum():
            right -= 1

        if s[left] != s[right]:
            return False

        left += 1
        right -= 1
    return True


def main():
    assert check_palindrome("abbba") == True
    assert check_palindrome("abb ba") == True
    assert check_palindrome("") == True
    assert check_palindrome("a") == True
    assert check_palindrome("aa") == True
    assert check_palindrome("aaa") == True
    assert check_palindrome("ab") == False
    assert check_palindrome("!, (?)") == True
    assert check_palindrome("12.02.2021") == True
    assert check_palindrome("21.02.2021") == False
    assert check_palindrome("hello, world") == False


if __name__ == "__main__":
    main()
