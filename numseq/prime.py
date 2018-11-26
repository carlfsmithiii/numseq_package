import math

def primes(num):
    """ Returns list of all primes <= num """
    return [n for n in range(num + 1) if is_prime(n)]

def is_prime(num):
    """ Returns True if num is prime, else False """
    if num % 2 == 0:
        return False
    for n in range(3, int(math.sqrt(num)) + 1, 2):
        if num % n == 0:
            return False
    return True
