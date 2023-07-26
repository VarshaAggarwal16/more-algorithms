# def isPrime(num : int):
#     for n in range(2, num//2):
#         if num%n == 0:
#             return False
#     return True

# print(isPrime(1000000007))

def is_prime(n):
    if n <= 1:
        return False
    if n <= 3:
        return True

    # Check if n is divisible by 2 or 3 (except for 2 and 3).
    if n % 2 == 0 or n % 3 == 0:
        return False

    # Use trial division method to check for prime.
    i = 5
    while i * i <= n:
        if n % i == 0 or n % (i + 2) == 0:
            return False
        i += 6

    return True

# Example usage
number_to_check = 1000000011
if is_prime(number_to_check):
    print(f"{number_to_check} is a prime number.")
else:
    print(f"{number_to_check} is not a prime number.")
