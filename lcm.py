def lcm(num1 : int, num2 : int) -> int:
    if num1 > num2:
        greater = num1  
    else:  
        greater = num2  
    while(True):  
        if((greater % num1 == 0) and (greater % num2 == 0)):  
            lcm = greater  
            break  
        greater += 1  
    return lcm
print(lcm(4, 6))
