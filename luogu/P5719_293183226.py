n, k = map(int, input().split())

sum_a = 0
cnt_a = 0
sum_b = 0
cnt_b = 0

for i in range(1, n + 1):
    if i % k == 0:
        sum_a += i
        cnt_a += 1
    else:
        sum_b += i
        cnt_b += 1

print(f"{sum_a / cnt_a:.1f}", f"{sum_b / cnt_b:.1f}")