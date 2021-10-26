from math import isqrt


def find_factors(n):
    factors = []
    # for i in range(1, n + 1):
    for i in range(1, isqrt(n)):
        if n % i == 0:
            factors.append(i)
    return factors


def is_prime(n):
    for i in range(2, n):
        if n % i == 0:
            return False
    else:
        return True


def create_prime_list(factors):
    prime_factors = []
    for element in factors:
        if is_prime(element):
            prime_factors.append(element)
    return prime_factors


def max_prime(prime_factors):
    return max(prime_factors)


def largest_prime_factor(n):
    factors = find_factors(n)
    prime_factors = create_prime_list(factors)
    max_prime_num = max_prime(prime_factors)
    return max_prime_num


if __name__ == "__main__":
    number = 13195
    number2 = 600851475143
    print(largest_prime_factor(number2))
