"""
The sum of the squares of the first ten natural numbers is,
The square of the sum of the first ten natural numbers is,
Hence the difference between the sum of the squares of the first ten natural numbers and the square of the sum is .
Find the difference between the sum of the squares of the first one hundred natural numbers and the square of the sum.
"""


def sum_of_the_square():
    sum = 0
    for i in range(1, 101):
        sum += i*i
    return sum


def square_of_the_sum():
    sum = 0
    for i in range(1, 101):
        sum += i
    sum *= sum
    return sum


if __name__ == "__main__":
    print(square_of_the_sum() - sum_of_the_square())
