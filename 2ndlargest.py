from math import inf
from typing import List
def secondLargestNumber(numbers : List[int]):
    max_number = -inf
    second_max= -inf
    for num in numbers:
        if num < second_max and num < max_number:
            pass
        elif num > second_max and num < max_number:
            second_max = num
        else:
            second_max = max_number
            max_number = num
    return second_max 
print(secondLargestNumber([5,3,4,1,2,]))

