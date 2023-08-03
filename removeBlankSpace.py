def removeBlankSpace(value : str):
    result = ""
    for char in value:
        if char == " ":
            pass
        else:
            result+= char
    return result 
print(removeBlankSpace("var sha"))