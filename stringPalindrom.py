def isPalindrome(value : str):
    value1 = value[::-1]
    return value == value1
print(isPalindrome("boby"))