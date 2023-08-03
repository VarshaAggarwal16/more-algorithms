def deleteVowels(value : str):
    vowels = ['a', 'e', 'i', 'o', 'u']
    result = ""
    for char in value:
        if char in vowels:
            pass
        else:
            result+= char
    return result
print(deleteVowels("varsha"))

