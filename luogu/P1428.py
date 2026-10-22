n = int(input())
a = list(map(int, input().split()))
for i in range(n):
    m = 0
    for j in range(i):
        if a[j] < a[i]:
            m += 1
    print(m, end=" ")