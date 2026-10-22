import math
a, b, c = sorted(map(int, input().split()))
print(f"{a//math.gcd(a,c)}/{c//math.gcd(a,c)}")
