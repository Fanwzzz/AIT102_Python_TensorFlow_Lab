k = int(input())

day = 0
coin = 1
ans = 0

while day < k:
    for _ in range(coin):
        if day == k:
            break

        ans += coin
        day += 1

    coin += 1

print(ans)