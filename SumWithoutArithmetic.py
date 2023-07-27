def add_without_arithmetic_operator(a, b):
    while b != 0:
        carry = a & b
        print(carry)
        a = a ^ b
        b = carry << 1
    return a

# Test the function
num1 = int(input("Enter the first integer: "))
num2 = int(input("Enter the second integer: "))

result = add_without_arithmetic_operator(num1, num2)
print("The sum of {} and {} is: {}".format(num1, num2, result))
