def fibonnacci(n):
    num1  = 0
    num2 = 1
    fibonacci_list = [num1, num2]
    for i in range(1, n-1):
        result = num1+num2
        num1 = num2
        num2 = result
        fibonacci_list.append(result)
    return fibonacci_list
print(fibonnacci(5))


def fibonacciAgain(n):
    #return code
    # if n<=0:
    #     return []
    # elif n==1:
    #     return [0]
    if n==2:
        return [0,1]

    #recursion code
    else:
        fib_list = fibonacciAgain(n-1)
    #backwards code

        fib_list.append(fib_list[-1] + fib_list[-2])

        return fib_list
    
print(fibonacciAgain(5))

 

