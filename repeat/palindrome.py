# def isPalindrome(num : int):
#     number = str(num)
#     result = number[::-1]
#     result = int(result)
#     return num == result
    
# print(isPalindrome(211)) 


# def isPalindrome(num : int):
#     n = num
#     result = 0
#     while(n>0): 
#         remainder = n%10
#         result = result*10 + remainder
#         n = n//10
#     return result == num
# print(isPalindrome(122))


def isPalindrome(num : int):
    n = num
    result = 0
    #return code
    if num<10:
        return num

    #forward code
    remainder = n%10
    n = n//10

    #recursion code
    r = isPalindrome(n)

    #backwards code
    result = result*10 + remainder
