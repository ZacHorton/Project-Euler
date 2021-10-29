"""
The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.
Find the sum of all the primes below two million.
"""
from math import isqrt


# Sieve of Eratosthenes
def summation_of_primes():
    primes = [True] * 2000000
    primes[0], primes[1] = False, False
    for i in range(2, isqrt(2000000)):
        for j in range(i*i, 2000000, i):
            if primes[j]:
                primes[j] = False
    list_of_primes = []
    for k in range(0, 2000000):
        if primes[k] is True:
            list_of_primes.append(k)

    sum_of_primes = 0
    for index, element in enumerate(list_of_primes):
        sum_of_primes += element
    print(sum_of_primes)


if __name__ == "__main__":
    summation_of_primes()
