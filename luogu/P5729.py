w, x, h = map(int, input().split())
cube = [[[True] * h for _ in range(x)] for _ in range(w)]

q = int(input())
l = []
for _ in range(q):
    l = list(map(int,input().split()))
    for i in range(l[0]-1,l[3]):
        for j in range(l[1]-1,l[4]):
            for k in range(l[2]-1,l[5]):
                cube[i][j][k] = False
print(sum(cell for plane in cube for row in plane for cell in row))