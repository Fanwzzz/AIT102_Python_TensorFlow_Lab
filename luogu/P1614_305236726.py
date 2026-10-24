n, m = map(int, input().split())
values = [int(input()) for _ in range(n)]

window_sum = sum(values[:m])
best = window_sum

for right in range(m, n):
    window_sum -= values[right - m]  # 移出左端的数
    window_sum += values[right]      # 移入右端的新数
    best = min(best, window_sum)

print(best)