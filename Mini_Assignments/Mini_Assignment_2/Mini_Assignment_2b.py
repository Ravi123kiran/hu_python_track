print("Diamond star pattern")
# Reading number of row
n = int(input('Enter number of row: '))

#Upper
for i in range(1, n + 1):
    for j in range(1, n - i + 1):
        print(" ", end="")
    for j in range(1, 2 * i):
        print("*", end="")
    print()

#lower
for i in range(n - 1, 0, -1):
    for j in range(1, n - i + 1):
        print(" ", end="")
    for j in range(1, 2 * i):
        print("*", end="")
    print()
