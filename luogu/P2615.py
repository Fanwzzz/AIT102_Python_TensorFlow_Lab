N = int(input())
m = [[0] * N for _ in range(N)]

row, col = 0, N // 2
m[row][col] = 1

for K in range(2, N * N + 1):
    if row == 0 and col == N - 1:
        row += 1
    elif row == 0 and col != N - 1:
        row = N - 1
        col += 1
    elif row != 0 and col == N - 1:
        row -= 1
        col = 0
    else:
        if m[row-1][col+1]:
            row += 1
        else:
            row -= 1
            col += 1
    m[row][col] = K

for i in m:
    print(*i)