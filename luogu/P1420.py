n = int(input())
a = list(map(int, input().split()))
best = 0

for i in range(len(a)):
    ct = 1
    for j in range(i+1, len(a)):
        if a[i]+(j-i) != a[j]:
            break
        else:
            ct += 1
    if ct >= best:
        best = ct
print(best)