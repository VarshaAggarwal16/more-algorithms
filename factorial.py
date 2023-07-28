def factorial(num : int):
    # return logic
    if num ==1:
        return 1
    
    # forward code
    #recursion call
    r = factorial(num-1)
    #backward code
    return num*r
print(factorial(3))


def factorialNumber(num :  int):
    result = 1
    while(num>=1):
        
        result*=num
        num-=1
    return result
print(factorialNumber(3))


def factorial1(num : int):

    result = 1
    for n in range(2, num+1):
        result = result*n
    return result
print(factorial1(5))

        