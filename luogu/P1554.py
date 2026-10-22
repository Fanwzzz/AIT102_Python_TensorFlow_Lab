M, N = map(int, input().split())

digits = "".join(map(str, range(M, N + 1)))
ct = [digits.count(str(d)) for d in range(10)]

print(*ct)