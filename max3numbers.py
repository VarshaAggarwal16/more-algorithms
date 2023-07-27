from math import inf
from typing import List
def maxNumber(nums : List[int]):
    if len(nums) == 0:
        raise ValueError("invalid value")
    max_num = -inf
    for num in nums:
        if num > max_num:
            max_num = num
    return max_num
print(maxNumber([-12, -10, -5]))

def maxOf3(num1: int, num2: int, num3: int):
    max = -inf
    if num1 > num2:
        if num1 > num3:
            max = num1
        else:
            max = num3
    else:
        if num2 > num3:
            max = num2
        else:
            max = num3
    return max

print(maxOf3(12, 10, 5))