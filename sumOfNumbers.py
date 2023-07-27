def sumOfDigitsOfANumber(num : int):
    #returning logic
    if num <10:
        return num

    #forward code
    remainder = num%10

    #recursion call
    r = sumOfDigitsOfANumber(num//10)

    #backward code
    return remainder + r
print(sumOfDigitsOfANumber(1234))