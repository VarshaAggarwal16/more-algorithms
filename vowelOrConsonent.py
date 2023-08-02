def isVowelOrConsonent(character : str):
    character1 : str = character.lower()
    vowels = ['a', 'e', 'i','o', 'u']
    if character1 in vowels :
        return (f"{character} is vowel")
    else:
        return (f"{character} is consonent")
print(isVowelOrConsonent("A"))