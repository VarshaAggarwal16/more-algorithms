def uppercaseVowels(value : str):
    vowels = ['a', 'e', 'i','o', 'u']
    result = ""
    for char in value:
        if char in vowels:
            result+= char.upper()
        else:
            result+= char
    return result
print(uppercaseVowels("hello world"))

