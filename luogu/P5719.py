n, k = map(int, input().split())

cnt_a = n // k
sum_a = k * cnt_a * (cnt_a + 1) // 2

sum_all = n * (n + 1) // 2

cnt_b = n - cnt_a
sum_b = sum_all - sum_a

print(f"{sum_a / cnt_a:.1f}", f"{sum_b / cnt_b:.1f}")