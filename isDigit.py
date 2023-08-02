def isDigit(value):
    if (value>='0' and value <='9'):
    # if '0' <= value <= '9':
        return (f"{value} is digit")
    else:
        return (f"{value} is not digit")
print(isDigit("2"))
        