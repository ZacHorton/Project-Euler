"""
By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see that the 6th prime is 13.
What is the 10 001st prime number?
"""
from math import isqrt


def sieve_of_eratosthenes():
    primes = [True] * 1000000
    primes[0], primes[1] = False, False
    for i in range(2, isqrt(1000000)):
        for j in range(i*i, 1000000, i):
            # print(f"i:{i}, j{j}")
            if primes[j]:
                primes[j] = False
    list_of_primes= []
    for k in range(0, 999999):
        if primes[k] is True:
            list_of_primes.append(k)

    for index, element in enumerate(list_of_primes):
        if index == 10000:
            print(element)


if __name__ == "__main__":
    sieve_of_eratosthenes()
