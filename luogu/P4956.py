N = int(input())
X_max, K_min = 0, 0
for X in range(1,101):
    for K in range(100,0,-1):
        if 52*(7*X+21*K) == N:
            X_max = X
            K_min = K
print(X_max)
print(K_min)