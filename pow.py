import math

def powMethod(base : int, exponent: int) -> int:
    result = 1
    if exponent <= 0:
        raise ValueError("Error")
    for n in range(1, exponent+1):
        result *= base
    return result
print(powMethod(3,2))

print(math.sqrt(26))

