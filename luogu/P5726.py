n = int(input())
a = sorted(map(int, input().split()))
a.pop(0)
a.pop()

s = 0
for i in range(len(a)):
    s += a[i]
print(f"{s/(n-2):.2f}")