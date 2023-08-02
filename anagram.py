def isAnagram(value1 : str, value2 : str):
    finalValue1 = value1.lower().replace(" ", "")
    finalValue2 = value2.lower().replace(" ", "")

    map1 = {}
    map2 = {}

    for c in finalValue1:
        map1[c] = map1.get(c, 0)+1

    for c in finalValue2:
        map2[c] = map2.get(c, 0)+1

    return map1 == map2
 

print(isAnagram("Clint Eastwood", "old west action"))