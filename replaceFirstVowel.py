def replaceFirstVowel(value : str):
    vowels = ['a', 'e', 'i', 'o', 'u']
    for i in range(len(value)):
        if value[i] in vowels:
            value = value[:i] + '-' + value[i+1:]
            break
    return value



print(replaceFirstVowel("varsha"))
