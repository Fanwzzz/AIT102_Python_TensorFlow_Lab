import math

n = int(input())

for i in range(2, math.isqrt(n)+1):
    if n%i == 0:
        print(n//i)
        break