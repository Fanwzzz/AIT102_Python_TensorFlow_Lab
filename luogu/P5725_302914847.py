n = int(input())

for i in range(n):
    for j in range(n):
        print(f"{i * n + j + 1:02d}", end="")
    print()

print()

num = 1
for i in range(n):
    print(" " * (2 * (n - 1 - i)), end="")
    for j in range(i + 1):
        print(f"{num:02d}", end="")
        num += 1
    print()