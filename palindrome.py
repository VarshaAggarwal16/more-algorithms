def isPalindrome(num : int):
    number = str(num)
    pal = number[: : -1]
    pal = int(pal)
    return pal == num
    
print(isPalindrome(121))

def isPalindrome2(nums : int):
    num = nums
    result = 0
    while(num>0):
        remainder = num%10
        result = result*10 + remainder
        num = num//10
    return nums == result

print(isPalindrome2(121))

def isPalindrome3(num : int):
    # return condition
    if(num < 10):
        return num
    #forward code
    m = num%10
    d = num//10
    # recursive call
    r = isPalindrome3(d)
    # backward code
    return int(str(m) + str(r))

print(isPalindrome3(1233435))

