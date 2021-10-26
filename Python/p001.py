def multiples_of_3_or_5():
    solution = 0
    for element in range(1, 1000):
        if element % 3 == 0 or element % 5 == 0:
            solution += element
    return solution


if __name__ == "__main__":
    print(multiples_of_3_or_5())
