n = int(input())
matrix = [[0] * n for _ in range(n)]
directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]

row, col = 0, 0
direction = 0

for i in range(1,n**2+1):
    matrix[row][col] = i

    if i == n**2:
        break

    dr, dc = directions[direction]
    next_row = row + dr
    next_col = col + dc

    if not( 0 <= next_row < n 
            and 0 <= next_col < n 
            and matrix[next_row][next_col] == 0):
        direction = (direction + 1) % 4
        dr, dc = directions[direction]
        next_row = row + dr
        next_col = col + dc
        
    row, col = next_row, next_col

for i in matrix:
    print("".join(f"{j:3d}" for j in i))