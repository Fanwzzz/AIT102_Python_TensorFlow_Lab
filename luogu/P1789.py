n, m, k = map(int, input().split())

torch = [tuple(map(int, input().split())) for _ in range(m)]
glowstone = [tuple(map(int, input().split())) for _ in range(k)]

matrix = [[0] * n for _ in range(n)]

for x, y in torch:
    row = x - 1 
    col = y - 1

    for dx in range(-2, 3):
        for dy in range(-2, 3):
            if abs(dx) + abs(dy) <= 2:
                r = row + dx
                c = col + dy
                
                if 0 <= r < n and 0 <= c < n:
                    matrix[r][c] = 1

for x, y in glowstone:
    row = x - 1 
    col = y - 1

    for dx in range(-2, 3):
        for dy in range(-2, 3):
            r = row + dx
            c = col + dy
            if 0 <= r < n and 0 <= c < n:
                matrix[r][c] = 1

print(sum(j == 0 for i in matrix for j in i))