def fibonacci():
    a = 1
    b = 2
    solution = 0
    while a <= 4000000:
        a, b = b, a + b
        if a % 2 == 0:
            solution += a
    return solution


if __name__ == "__main__":
    print(fibonacci())
