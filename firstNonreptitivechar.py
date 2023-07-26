def first_non_repeating_char(s):
    char_freq = {}
    
    # Count the frequency of each character in the string
    for char in s:
        char_freq[char] = char_freq.get(char, 0) + 1

    # Find the first non-repeating character in the string
    for char in s:
        if char_freq[char] == 1:
            return char

    # If no non-repeating character is found, return None or any appropriate value
    return None

# Example usage:
input_string = "varshav"
result = first_non_repeating_char(input_string)
print(result)  # Output: 'c'


