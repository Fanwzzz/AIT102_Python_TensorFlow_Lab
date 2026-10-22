import math
a, b, c = input().split()
a, b, c = float(a), float(b), float(c)
p = (a+b+c)/2
s = math.sqrt(p*(p-a)*(p-b)*(p-c))
print(f"{s:.1f}")