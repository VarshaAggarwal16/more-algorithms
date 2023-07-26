def fibonacci(num : int):
    if num<0:
        raise ValueError("invalid value")
    num1 = 0
    num2 = 1
    arr = [num1, num2]
    for i in range(1, num-1):
        result = num1 + num2
        num1 = num2
        num2 = result
        arr.append(result)
    return arr
print(fibonacci(10))


def fibonacci_list(n):
    if n <= 0:
        return []  # Fibonacci series is not defined for n <= 0
    elif n == 1:
        return [0]
    elif n == 2:
        return [0, 1]
    else:
        fib_list = fibonacci_list(n - 1)
        fib_list.append(fib_list[-1] + fib_list[-2])
        return fib_list

# Example usage
num_terms = 10
fib_numbers = fibonacci_list(num_terms)
print(f"The Fibonacci numbers up to {num_terms} terms are: {fib_numbers}")


