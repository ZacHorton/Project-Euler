arr = list(range(1, 1000))
solution = 0
for element in arr:
    if element % 3 == 0:
        solution += element
    elif element % 5 == 0:
        solution += element
print(solution)