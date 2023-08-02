# def removeChar(value, character):
 
#       print(value.replace(character, ""))
    
# removeChar("varsha", "v")


def removeChar(value, character):
    finalValue = ""
    # result_list = [char for char in value]
    for char in value:
        if char == character:
            pass
        else:
            finalValue+= char
    return finalValue
    


print(removeChar("varsha", "a"))

def replaceSpace(value : str, character : str):
    result = ""
    for char in value:
        if char == " ":
            result+= character
        else:
            result+= char
    return result
print(replaceSpace("va sha", "r"))

