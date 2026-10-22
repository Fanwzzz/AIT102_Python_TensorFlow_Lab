s_1, s_2, s_3 = map(int, input().split())
ct = [0] * (s_1+s_2+s_3 - 2)

for i in range(1,s_1+1):
    for j in range(1,s_2+1):
        for k in range(1,s_3+1):
            ct[i+j+k-3] += 1

print(ct.index(max(ct)) + 3)