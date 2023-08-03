def copyString(value : str):
    value1 = ""
    for char in value:
        value1+= char
    return value1
print(copyString("i love norway"))

string = input("Please Enter a string: ")
new_string = string[:]
print("New String After Copy:", new_string)
