# def firstNPrimes(n : int):
#     result = []
#     if n > 1:
#         result.append(1)
    
#     if n > 2:
#         result.append(2)
    
#     if n > 3:
#         result.append(3)

#     # 5 + 6k, 5 + 6k +2
#     k=0
#     while(True):
#        a = 5 + 6 * k 
#        b = 5 + 6 * k + 2
#        if(a > n):
#            break
#        else:
#            result.append(a)
#        if(b > n ):
#            break
#        else:
#            result.append(b)
#        k+=1
#     return result

# print(firstNPrimes(50))

def is_prime(num):
    if num <= 1:
        return False
    if num <= 3:
        return True
    if num % 2 == 0 or num % 3 == 0:
        return False
    i = 5
    while i * i <= num:
        if num % i == 0 or num % (i + 2) == 0:
            return False
        i += 6
    return True

def print_first_n_primes(n):
    count = 0
    num = 2
    prime_numbers = []
    while count < n:
        if is_prime(num):
            prime_numbers.append(num)
            count += 1
        num += 1
    return prime_numbers

if __name__ == "__main__":
    n = int(input("Enter the value of n: "))
    if n <= 0:
        print("Please enter a positive integer.")
    else:
        print("First", n, "prime numbers are:")
        primes = print_first_n_primes(n)
        print(", ".join(str(p) for p in primes))

        