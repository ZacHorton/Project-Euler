"""
2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.
What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?
"""


def smallest_multiple_of_10():
    num = 1
    restart = True
    while restart:
        for x in range(1, 11):
            if num % x != 0:
                num += 1
                break
        else:
            restart = False
    return num


def smallest_multiple_of_20():
    num = 1
    restart = True
    while restart:
        for x in range(1, 21):
            if num % x != 0:
                num += 1
                break
        else:
            restart = False
    return num


if __name__ == "__main__":
    # print(smallest_multiple_of_10())
    print(smallest_multiple_of_20())