def revNumber(num : int):
    intNum = str(num)
    revnum = intNum[: : -1]
    result = int(revnum)

    return result
print(revNumber(12345))


def numrev(nums : int):
    result = 0
    while(nums>0):
        remainder = nums%10
        result = result*10 + remainder
        nums = int(nums/10)
    return result

print(numrev(12345))

