# def nonRepeatingChar(value : str):
#     map = {}
#     result = ""
#     for char in value:
#         map[char] = map.get(char,0) +1
#     for char in value:
#         if map[char] == 1:
#             result+= char
#     return result
# print(nonRepeatingChar("pythonprogramming"))

def nonRepeatingChar(value : str):
    map = {}
    result = ""
    for char in value:
        map[char] = map.get(char,0) +1
    for k,v in map.items():
        if v == 1:
            result+= k
    return result
print(nonRepeatingChar("pythonprogramming"))
