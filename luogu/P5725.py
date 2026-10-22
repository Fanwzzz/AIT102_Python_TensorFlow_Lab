n = int(input())

for i in range(n):
    for j in range(n):
        print(f"{i * n + j + 1:02d}", end="")
    print()

print()

for i in range(n):
    print(" " * (2 * (n - 1 - i)), end="")
    for j in range(i + 1):
        print(f"{i*(i+1)//2+j+1:02d}", end="")
    print()