n, m = map(int, input().split())
ls = [int(input()) for _ in range(n)]
best = sum(ls[:m])

for i in range(1,n-m+1):
    sum = 0
    for j in range(i,i+m):
        sum += ls[j]
    if sum < best:
        best = sum
print(best)