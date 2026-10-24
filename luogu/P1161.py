n = int(input())

lights = [False] * (2000001)

for _ in range(n):
    a, t = input().split()
    a, t = int(a.replace(".", "")), int(t)

    for j in range(1, t+1):
        n = a * j // 1000000
        lights[n] = not lights[n]

print(lights.index(True))
        