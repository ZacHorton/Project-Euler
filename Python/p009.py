"""
A Pythagorean triplet is a set of three natural numbers, a < b < c, for which,
a^2 + b^2 = c^2
For example, 3^2 + 4^2 = 9 + 16 = 25 = 5^2.
There exists exactly one Pythagorean triplet for which a + b + c = 1000.
Find the product abc.
"""


# Euclid's Formula
# a = m^2 - n^2, b = 2mn, c = m^2 + n^2
def pythagorean_triplet():
    for m in range(1, 21):
        for n in range(1, 6):
            if m > n:
                a = (m * m - n * n)
                b = (2 * m * n)
                c = (m * m + n * n)
                if a + b + c == 1000:
                    return a * b * c


if __name__ == "__main__":
    print(pythagorean_triplet())
