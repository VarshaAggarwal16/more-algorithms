def isBinary(num : int):
    while(num>0):
        if num%10 not in [0,1]:
            return False
        num = num//10
    return True
print(isBinary(1011))
