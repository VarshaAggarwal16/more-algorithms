def countCharDigit(value : str):
    countDigit = 0
    countAlphabet = 0
    countSpecialChar = 0

    for char in value:
        if  '0' <= char <= '9': 
            countDigit += 1
        elif 'a' <= char <= 'z' or 'A' <= char <= 'Z':
            countAlphabet += 1
        else:
            countSpecialChar += 1
    return (f"countDigit is {countDigit}, countAlphabet is {countAlphabet}, countSpecialChar is {countSpecialChar}")
print(countCharDigit("!@#Varsha1234"))


