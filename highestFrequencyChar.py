def highestFrequencyChar(value : str):
    value1 = value.replace(" ", "")
    charFrquency = {}
    for char in value1:
        charFrquency[char] = charFrquency.get(char,0) +1
    max_freq = max(charFrquency.values())
    for char in value1:
        if charFrquency[char] == max_freq:
            return char
print(highestFrequencyChar("I love Norway"))

