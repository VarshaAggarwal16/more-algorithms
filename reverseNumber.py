def reverse_number_string(num):
    num_str = str(num)
    reversed_str = num_str[::-1]
    reversed_num = int(reversed_str)
    return reversed_num

print(reverse_number_string(12345))