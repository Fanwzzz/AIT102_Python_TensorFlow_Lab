h = []
for i in range(1,8):
    t = list(map(int, input().split()))
    h.append(t[0]+t[1])
if max(h)<=8:
    print(0)
else:
    print(h.index(max(h))+1)