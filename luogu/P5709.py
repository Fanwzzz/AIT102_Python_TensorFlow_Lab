m, t, s = map(int, input().split())
if t == 0 or s >= m*t:
    print(0)
else:
    print(m-((s+t-1)//t))