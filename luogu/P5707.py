import math
s, v = map(int, input().split())
t = 480 - (math.ceil(s/v) + 10)
if t < 0:
    t += 24*60
print(f"{t//60:02d}:{t%60:02d}")