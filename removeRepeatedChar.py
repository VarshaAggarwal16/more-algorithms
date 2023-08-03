def removeRepeatedChar(value : str):
    map = {}
    result = ""
    for char in value:
        count = map.get(char,0)
        if count == 0:
            map[char] = 1
            result+= char
    return result
print(removeRepeatedChar("varsha"))