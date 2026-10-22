l, m = map(int, input().split())
tree = [True] * (l+1)

for _ in range(m):
    u, v = map(int, input().split())
    for i in range(u, v+1):
        tree[i] = False
print(tree.count(True))