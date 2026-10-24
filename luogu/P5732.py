n = int(input())
ls = [1]

for i in range(1, n+1):
    print(" ".join(map(str, ls)))

    next_ls = [0] * (i+1)
    for j in range(i+1):
        next_ls[j] = (0 if j-1 < 0 else ls[j-1]) + (0 if j > i-1 else ls[j])
    ls = next_ls