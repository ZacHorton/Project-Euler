"""
If we list all the natural numbers below 10 that are multiples of 3 or 5, we get 3, 5, 6 and 9.
The sum of these multiples is 23.
Find the sum of all the multiples of 3 or 5 below 1000.
"""


def multiples_of_3_or_5():
    solution = 0
    for element in range(1, 1000):
        if element % 3 == 0 or element % 5 == 0:
            solution += element
    return solution


if __name__ == "__main__":
    print(multiples_of_3_or_5())
