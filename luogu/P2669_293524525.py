k = int(input())

coin = 1
cnt = 0
ans = 0

for _ in range(k):
    ans += coin
    cnt += 1
    if coin == cnt:
        coin += 1
        cnt = 0
print(ans)