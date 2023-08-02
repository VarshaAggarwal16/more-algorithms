def isArmstrong(nums : int):
    num = nums
    length = len(str(num))
    sum = 0
    while(num>0):
        remainder = num%10
        sum += remainder**length
        num = num//10
    return sum == nums
print(isArmstrong(153))

