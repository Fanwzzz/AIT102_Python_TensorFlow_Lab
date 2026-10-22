n = int(input())
S = 0
for i in range(n):
    fac = 1
    for j in range(i+1):
        fac *= (j+1)
    S += fac
print(S)