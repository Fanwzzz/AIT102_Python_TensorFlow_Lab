n, k = map(int, input().split())
l = []
dl = []
for i in range(1,n+1):
    if i%k==0:
        l.append(i)
    else:
        dl.append(i)
s = 0
ds = 0
for i in l:
    s+=i
for i in dl:
    ds+=i
print(f"{s/len(l):.1f}",f"{ds/len(dl):.1f}")