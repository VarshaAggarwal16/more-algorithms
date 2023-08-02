# def countGivenCharacter(value : str, character : str):
#     print(value.count(character))
# countGivenCharacter("an apple a day keeps doctor away", "a")

def countGivenCharacter(value : str, character : str):
    map = {}
    for c in value:
        map[c] = map.get(c, 0) +1
    return map.get(character)
print(countGivenCharacter("an apple a day keeps doctor away", "a"))