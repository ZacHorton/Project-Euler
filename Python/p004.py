"""
A palindromic number reads the same both ways.
The largest palindrome made from the product of two 2-digit numbers is 9009 = 91 × 99.
Find the largest palindrome made from the product of two 3-digit numbers.
"""


def is_palindrome(n):
    number = str(n)
    if len(number) == 4:
        if number[0] == number[3] and number[1] == number[2]:
            return True
        elif number[0] != number[3] or number[1] != number[2]:
            return False
    elif len(number) == 5:
        if number[0] == number[4] and number[1] == number[3]:
            return True
        elif number[0] != number[4] or number[1] != number[3]:
            return False
    elif len(number) == 6:
        if number[0] == number[5] and number[1] == number[4] and number[2] == number[3]:
            return True
        elif number[0] != number[5] or number[1] != number[4] or number[2] != number[3]:
            return False
    else:
        return "unknown"


def largest_palindrome_using_product_of_two_2_digit_numbers():
    xy = 0
    for x in range(10, 100):
        for y in range(10, 100):
            if is_palindrome(x * y):
                xy = x * y
    return xy


def largest_palindrome_using_product_of_two_3_digit_numbers():
    xy = 0
    for x in range(100, 1000):
        for y in range(100, 1000):
            if is_palindrome(x * y):
                if x * y > xy:
                    xy = x * y
    return xy


if __name__ == "__main__":
    # print(largest_palindrome_using_product_of_two_2_digit_numbers())
    print(largest_palindrome_using_product_of_two_3_digit_numbers())



