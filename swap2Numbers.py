a = int(input("please give first number a: "))
b = int(input("please give second number b: "))
a=a-b
b=a+b
a=b-a
print("After swapping")
print("value of a is : ", a);
print("value of b is : ", b); 



def swapNumbers(num1 : int, num2 : int):
    num3 = num1
    num1 = num2
    num2 = num3
    return num1, num2
print(swapNumbers(12,10))