def perfectNumber(num : int):
    n = 1
    numbers = []
    while(n<=num/2):
        if not num%n:
            numbers.append(n)
        n+=1
        
    return num == sum(numbers)

print(perfectNumber(6))
