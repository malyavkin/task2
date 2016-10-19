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
    return num


def factorize(n):
    factors = []
    while n > 1:
        for i in range(2, n + 1):
            if n % i == 0:
                n //= i
                factors.append(i)
                break
    return factors