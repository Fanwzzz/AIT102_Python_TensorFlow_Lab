k = int(input())
d = 0
ans = 0
for i in range(k):
    for j in range(i+1):
        ans += i+1
        d += 1
        if d >= k:
            break
    if d >= k:
        break
print(ans)