n = int(input())
ls = list(map(int, input().split()))
ct = [False] * n

for i in range(n):
    for j in range(i+1,n):
        if ls[i] + ls[j] in set(ls):
            ct[ls.index(ls[i] + ls[j])] = True
print(ct.count(True))