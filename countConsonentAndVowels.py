def countConsonentAndVowels(value : str):
    vowels = ['a', 'e', 'i', 'o', 'u']
    consonentcount = 0
    vowelscount = 0
    for char in value:
        if char in vowels:
            vowelscount += 1
        else:
            consonentcount+= 1
    return vowelscount, consonentcount
print(countConsonentAndVowels("varsha"))
