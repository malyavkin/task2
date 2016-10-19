from math import sqrt


def is_prime(n):
    j = 2
    while j <= int(sqrt(n)):
        if n % j == 0:
            return False
        j += 1
    return True

def find_nth_prime(n):
    prime_count = 0
    num = 1
    while prime_count < n:
        num += 1
        if is_prime(num):
            prime_count += 1
            if prime_count % 5000 == 0:
                print(prime_count)
    return num
