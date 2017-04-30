#! python3


def is_prime(n):
    if n < 2:
        return False
    d = int(n/2 + 0.5)
    for i in range(2, d):
        if n % i == 0:
            return False
    else:
        return True


def primes(n):
    for i in range(0, n):
        if is_prime(i):
            yield i


for prime in primes(n=100):
    print(prime, end='  ')
