n = int(input())
c = 0
for i in range(n):
    for j in range(n-i):
        c += 1
        print(f"{c:02d}", end="")
    print(end="\n")