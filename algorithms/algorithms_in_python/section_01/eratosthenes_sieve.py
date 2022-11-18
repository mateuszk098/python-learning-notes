"""
Write an algorithm to print all prime numbers smaller than n.
Sieve of Eratosthenes version.

Description: https://en.wikipedia.org/wiki/Sieve_of_Eratosthenes
"""


def eratosthenes_sieve(n):
    """Uses Sieve of Eratosthenes to find prime numbers smaller than n."""
    tmp = [True] * n
    i = 2

    while i * i < n:
        if tmp[i] == True:
            for k in range(i * i, n, i):  # Multiples of i are not primes.
                tmp[k] = False
        i += 1

    return tmp


primes = eratosthenes_sieve(101)
for index, tmp in enumerate(primes):
    if tmp and index > 1:
        print(index, end=" ")
