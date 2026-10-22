x, n = map(int, input().split())
ans = 0
for k in range(n):
    day = (x-1+k)%7+1
    if day <= 5:
        ans+=250
print(ans)