def sumOfIntegers(value : str):
    sum = 0
    for char in value:
        if '0'<= char <='9':
            sum+= int(char)
    return sum
    

print(sumOfIntegers("123fshgdhh@@@@"))