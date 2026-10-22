a, b, c = input().split()
a, b, c = float(a), float(b), float(c)
p = (a+b+c)/2
s = (p*(p-a)*(p-b)*(p-c))**0.5
print(f"{s:.1f}")