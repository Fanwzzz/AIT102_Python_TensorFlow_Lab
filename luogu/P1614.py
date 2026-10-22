n, m = map(int, input().split())
ls = [int(input()) for _ in range(n)]
best = 10000000000

for i in range(0,n-m+1):
    sum = 0
    for j in range(i,i+m):
        sum += ls[j]
    if sum < best:
        best = sum
print(best)