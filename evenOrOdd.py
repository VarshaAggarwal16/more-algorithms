def isEven(num : int):
    if not num%2:
        return True
    else:
        return False
    
print(isEven(11))


def isEven1(num : int):
    if num%2==0:
        return True
    else:
        return False
    
print(isEven1(4))


def isEven2(num : int):
    return num%2==0

print(isEven2(4))